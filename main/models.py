from django.db import models
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import Account
from django.db import (
    DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY, DatabaseError, connection,
    connections, router, transaction,
)
from django.db.models.deletion import CASCADE, Collector




class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index = True,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Account, on_delete=models.PROTECT, null=True,blank=True)
    is_deleted = models.BooleanField(default=False)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print("save  ///")
        print("using  ///",using)
        print("update_fields  ///",update_fields)
        print("force_update  ///",force_update)
        print("force_insert  ///",force_insert)
        print("self  ///",self)
        
        """
        Save the current instance. Override this in a subclass if you want to
        control the saving process.

        The 'force_insert' and 'force_update' parameters can be used to insist
        that the "save" must be an SQL insert or update (or equivalent for
        non-SQL backends), respectively. Normally, they should not be set.
        """
        # Ensure that a model instance without a PK hasn't been assigned to
        # a ForeignKey or OneToOneField on this model. If the field is
        # nullable, allowing the save() would result in silent data loss.
        for field in self._meta.concrete_fields:
            # If the related field isn't cached, then an instance hasn't
            # been assigned and there's no need to worry about this check.
            if field.is_relation and field.is_cached(self):
                obj = getattr(self, field.name, None)
                print(obj)
                # A pk may have been assigned manually to a model instance not
                # saved to the database (or auto-generated in a case like
                # UUIDField), but we allow the save to proceed and rely on the
                # database to raise an IntegrityError if applicable. If
                # constraints aren't supported by the database, there's the
                # unavoidable risk of data corruption.
                if obj and obj.pk is None:
                    # Remove the object from a related instance cache.
                    if not field.remote_field.multiple:
                        field.remote_field.delete_cached_value(obj)
                    raise ValueError(
                        "save() prohibited to prevent data loss due to "
                        "unsaved related object '%s'." % field.name
                    )
                # If the relationship's pk/to_field was changed, clear the
                # cached relationship.
                if obj and getattr(obj, field.target_field.attname) != getattr(self, field.attname):
                    field.delete_cached_value(self)

        using = using or router.db_for_write(self.__class__, instance=self)
        print("usingss  ///", router.db_for_write(self.__class__, instance=self))

        if force_insert and (force_update or update_fields):
            raise ValueError("Cannot force both insert and updating in model saving.")

        deferred_fields = self.get_deferred_fields()
        if update_fields is not None:
            print("if /////")
            # If update_fields is empty, skip the save. We do also check for
            # no-op saves later on for inheritance cases. This bailout is
            # still needed for skipping signal sending.
            if not update_fields:
                return

            update_fields = frozenset(update_fields)
            field_names = set()

            for field in self._meta.fields:
                if not field.primary_key:
                    field_names.add(field.name)

                    if field.name != field.attname:
                        field_names.add(field.attname)

            non_model_fields = update_fields.difference(field_names)

            if non_model_fields:
                raise ValueError("The following fields do not exist in this "
                                 "model or are m2m fields: %s"
                                 % ', '.join(non_model_fields))

        # If saving to the same database, and this model is deferred, then
        # automatically do a "update_fields" save on the loaded fields.
        elif not force_insert and deferred_fields and using == self._state.db:
            print("else /////")
            
            field_names = set()
            for field in self._meta.concrete_fields:
                if not field.primary_key and not hasattr(field, 'through'):
                    field_names.add(field.attname)
            loaded_fields = field_names.difference(deferred_fields)
            if loaded_fields:
                update_fields = frozenset(loaded_fields)

        self.save_base(using=using, force_insert=force_insert,
                       force_update=force_update, update_fields=update_fields)
    save.alters_data = True



    def delete(self, using=None, keep_parents=False):

        print("delete //")
        using = using or router.db_for_write(self.__class__, instance=self)
        assert self.pk is not None, (
            "%s object can't be deleted because its %s attribute is set to None." %
            (self._meta.object_name, self._meta.pk.attname)
        )

        collector = Collector(using=using)
        collector.collect([self], keep_parents=keep_parents)
        return collector.delete()

    delete.alters_data = True

    class Meta:
        abstract = True
