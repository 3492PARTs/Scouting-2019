import cloudinary
import cloudinary.uploader
from flask import url_for
from peewee import *

import models as db


class query(object):
    """A library of convenient database access methods. Ideally, all of the
    database interaction should be in this class.

    When this class is instantiated, cloudinary is automatically configured."""

    def __init__(self):
        cloudinary.config(
            cloud_name="hbcgsvmyc",
            api_key="483847116472347",
            api_secret="UYew22cMiFrua6LbuHUQey40ahE"
        )


    # Start Jason's code

    def getAllUsers(self, page_num, page_size, return_total=False):
        users = db.user.select().where(db.user.active).join(db.user_roles, JOIN_INNER,
                                                            db.user.user_id == db.user_roles.user).order_by(
            db.user_roles.role)

        if return_total:
            total = users.count()
            return total, users.paginate(page_num, page_size)
        else:
            return users.paginate(page_num, page_size)

    def getSearchedUsers(self, search, page_num, page_size, return_total=False):
        users = db.user.select().where(
            db.user.active & (db.user.username.contains(search) | db.user.email.contains(search))).join(db.user_roles,
                                                                                                        JOIN_INNER,
                                                                                                        db.user.user_id == db.user_roles.user).order_by(
            db.user_roles.role)

        # users = db.user.select().where(db.user.active & db.user.email.contains(search)).paginate(page_num, num_of_pages)

        if return_total:
            total = users.count()
            return total, users.paginate(page_num, page_size)
        else:
            return users.paginate(page_num, page_size)

    def getUserCount(self):
        usercount = db.user.select().count()
        return usercount

    def getSearchedUserCount(self, search):
        usercount = db.user.select().where(db.user.active & db.user.email.contains(search)).count()
        return usercount

    def getAllRoles(self):
        roles = db.role.select(db.role.role_nm)
        return roles

    def updateUserRole(self, a, r):
        user = db.user.select(db.user.user_id).where(db.user.user_id == a)
        userrole = db.user_roles.get(db.user_roles.user == user)
        roleid = db.role.select(db.role.role_id).where(db.role.role_nm == r)
        userrole.role = roleid
        userrole.save()

    def softDeleteUser(self, u_id):
        user = db.user.get(db.user.user_id == u_id)
        user.active = False
        user.save()

    def role(self, id):
        role = db.role.select(db.role.role_nm).join(db.user_roles, JOIN_INNER, db.role.role_id ==
                                                    db.user_roles.select(db.user_roles.role).where(
                                                        db.user_roles.user == id)).tuples()
        role = list(role)[0][0]
        return role

    def getEmailJ(self, u_id):
        try:
            email = db.user.get(db.user.user_id == u_id)
            return email.email
        except DoesNotExist:
            print("FUCK")
            return None

    def getfName(self, u_id):
        try:
            name = db.user.get(db.user.user_id == u_id)
            print(name)
            return name.first_name
        except DoesNotExist:
            return None

    def getlName(self, u_id):
        try:
            lName = db.user.get(db.user.user_id == u_id)
            print(lName)
            return lName.last_name
        except DoesNotExist:
            return None



    def updateEmail(self, u_id, email):
        u = db.user.get(db.user.user_id == u_id)
        u.email = email
        u.save()

    def updateName(self, u_id, fname, lname):
        u = db.user.get(db.user.user_id == u_id)

        u.first_name = fname
        u.last_name = lname
        u.save()

    # End Jason's code

    # Begin Charlie's code
    def obtainFromCloudinary(self, img_id, img_ver):
        if img_id == '' or img_id is None or img_ver == '' or img_ver is None:
            return '/static/none.png'
        else:
            return cloudinary.CloudinaryImage(img_id, version=img_ver).build_url()


    def getAvatar(self, psyc_id):
        '''Returns the URL for a psychologist's avatar.

        :param int psyc_id: The ID of the psychologist.
        :return: The URL of the psychologist's avatar.
        :rtype: str'''
        psyc = db.psychologist.get(db.psychologist.psyc_id == psyc_id)
        if psyc.photo is None or psyc.photo == '':
            return url_for('static', filename='contents/icons/profile.svg')

        public_id, version = psyc.photo.split('#')

        return cloudinary.CloudinaryImage(public_id, version=version).build_url()

    def allowed_file(self, filename):
        '''Returns whether a filename's extension indicates that it is an image.

        :param str filename: A filename.
        :return: Whether the filename has an recognized image file extension
        :rtype: bool'''
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    def updateAvatar(self, psyc_id, avatar_file):
        '''Updates the avatar of a psychologist.

        :param int psyc_id: The ID of the psychologist.
        :param file avatar_file: A filelike object found in **flask.request.files**.
        :return: True if successful, False if unsuccessful.
        :rtype: bool'''
        if not self.allowed_file(avatar_file.filename):
            return False

        response = cloudinary.uploader.upload(avatar_file)
        image_descriptor = response['public_id'] + '#' + str(response['version'])

        p = db.psychologist.get(db.psychologist.psyc_id == psyc_id)
        p.photo = image_descriptor
        p.save()

        return True