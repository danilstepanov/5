__author__ = 'stepanov'
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, LargeBinary, MetaData, PrimaryKeyConstraint, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship, backref
from datetime import datetime


Base = declarative_base()
Base.metadata = MetaData(schema='ssrv')

Fbase = declarative_base()
Fbase.metadata = MetaData(schema='fwkeys')

class FirmwarKeys(Fbase):
    __tablename__='ssrv_firmware_keys'

    fwky_id = Column(Integer, primary_key=True)
    dvcl_dvcl_id = Column(Integer)
    pttp_pttp_id = Column(Integer)
    stbm_stbm_id = Column(Integer)
    key_name = Column(String)
    key_value = Column(String)
    rom_key_index = Column(Integer)
    rom_id = Column(Integer)
    ins_key_date = Column(TIMESTAMP)
    ins_date = Column(TIMESTAMP)

class LadderKeys(Fbase):
    __tablename__ = 'ssrv_ladder_keys'

    kmbk_value = Column(String , primary_key=True)
    ins_date = Column(TIMESTAMP)

class Group(Base):
    __tablename__='auth_group'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Permission(Base):
    __tablename__="auth_permission"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content_type_id = Column(Integer, primary_key=True)
    codename = Column(String)

class GroupPermissions(Base):
    __tablename__="auth_group_permissions"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey(Group.id))
    permission_id = Column(Integer, ForeignKey(Permission.id))

class User(Base):
    __tablename__="auth_user"
    id = Column(Integer, primary_key=True)
    password = Column(String)
    last_login = Column(TIMESTAMP)
    is_superuser = Column(Integer)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    is_staff = Column(Integer)
    is_active = Column(Integer)
    date_joined = Column(TIMESTAMP)

class Groups(Base):
    __tablename__="auth_user_groups"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    group_id = Column(Integer, ForeignKey(Group.id))

class UserUserPermissions(Base):
    __tablename__="auth_user_user_permissions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    permission_id = Column(Integer, ForeignKey(Permission.id))

class SignServerPermission(Base):
    __tablename__="signserver_permission"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    can_approve = Column(Integer)
    can_sign = Column(Integer)

class ProductGroup(Base):
    __tablename__="signserver_productgroup"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class SignScript(Base):
    __tablename__="signserver_signscript"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    script_zip = Column(String)

class Sproduct(Base):
    __tablename__="signserver_sproduct"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    product_group_id = Column(Integer, ForeignKey(ProductGroup.id))
    sign_script_id = Column(Integer, ForeignKey(SignScript.id))
    aprove_needed = Column(Integer)
    is_drm = Column(Integer)

class SproductEmail(Base):
    __tablename__="signserver_sproduct_emails"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    sproduct_id = Column(Integer, ForeignKey(Sproduct.id))

class SignFile(Base):
    __tablename__="signserver_signfile"
    id = Column(Integer, primary_key=True)
    blank_file = Column(String)
    sign_file_hash = Column(String)
    aprove = Column(Integer)
    refuse = Column(Integer)
    ready = Column(Integer)
    fail = Column(Integer)
    command_line = Column(String)
    when_signed = Column(TIMESTAMP)
    when_approved_or_refused = Column(TIMESTAMP)
    comment = Column(String)
    version_field = Column(String)
    product_id = Column(Integer, ForeignKey(ProductGroup.id))
    user_id = Column(Integer, ForeignKey(User.id))
    whom_approved_or_refused_id = Column(Integer, ForeignKey(User.id))