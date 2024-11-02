import psycopg2
from psycopg2 import sql
import bcrypt
import getpass

# Function to create a new user and put it in the database
def create_new_user(first_name, last_name, user_email, user_password):
    try:
        # Make DB connection
        conn = psycopg2.connect(
            dbname='using_sql_with_python',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )
        
        cursor = conn.cursor()

        # Insert the new user
        insert_query = sql.SQL(""" 
            INSERT INTO public.users (first_name, last_name, user_email, user_password)
            VALUES (%s, %s, %s, %s);
        """)

        cursor.execute(insert_query, (first_name, last_name, user_email, user_password.decode('utf-8')))  # Decode bytes to string

        conn.commit()

        print('Account successfully created!')

    except Exception as e:
        print(f'There was an error: {e}')

    finally:
        # Disconnect from DB
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def check_email(user_email):
    try:
        # Make DB connection
        conn = psycopg2.connect(
            dbname='using_sql_with_python',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )
        
        cursor = conn.cursor()

        # Check if email exists
        check_query = sql.SQL("""
            SELECT EXISTS (
                SELECT 1
                FROM public.users
                WHERE user_email = %s
            );
        """)
        
        cursor.execute(check_query, (user_email,))
        exists = cursor.fetchone()[0]

        return True
    
    except Exception as e:
        print(f'There was an error: {e}')
        return False

    finally:
        # Disconnect from DB
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def check_user_password(user_email, user_password):
    try:
        # Make DB connection
        conn = psycopg2.connect(
            dbname='using_sql_with_python',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )

        cursor = conn.cursor()

        # Query to get the hashed password for the provided email
        query = "SELECT user_password FROM public.users WHERE user_email = %s;"
        cursor.execute(query, (user_email,))
        result = cursor.fetchone()

        if result:
            hashed_password = result[0].encode('utf-8')  # Encode string back to bytes
            # Verify the provided password against the hashed password
            if bcrypt.checkpw(user_password.encode(), hashed_password):
                return True
            else:
                return False
        else:
            return False  # User does not exist

    except Exception as e:
        print(f'There was an error: {e}')
        return False

    finally:
        # Disconnect from DB
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_user_by_email(user_email):
    try:
        # Make DB connection
        conn = psycopg2.connect(
            dbname='using_sql_with_python',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )
        
        cursor = conn.cursor()

        # SQL command to delete the user
        delete_query = sql.SQL("""
            DELETE FROM public.users 
            WHERE user_email = %s;
        """)

        cursor.execute(delete_query, (user_email,))
        
        # Commit changes
        conn.commit()

    except Exception as e:
        print(f'There was an error: {e}')

    finally:
        # Disconnect from DB
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_user_email(current_email, new_email):
    try:
        # Make DB connection
        conn = psycopg2.connect(
            dbname='using_sql_with_python',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )
        
        cursor = conn.cursor()

        # SQL command to update the user email
        update_query = sql.SQL("""
            UPDATE public.users 
            SET user_email = %s 
            WHERE user_email = %s;
        """)

        cursor.execute(update_query, (new_email, current_email))
        
        # Commit changes
        conn.commit()

        if cursor.rowcount > 0:
            print(f'Successfully updated email from {current_email} to {new_email}.')
        else:
            print(f'No user found with the email: {current_email}')

    except Exception as e:
        print(f'There was an error: {e}')

    finally:
        # Disconnect from DB
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_user_password(user_email, new_password):
    try:
        # Make DB connection
        conn = psycopg2.connect(
            dbname='using_sql_with_python',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )
        
        cursor = conn.cursor()

        # Hash the new password
        hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode('utf-8')  # Decode to string

        # SQL command to update the user password
        update_query = sql.SQL(""" 
            UPDATE public.users 
            SET user_password = %s 
            WHERE user_email = %s;
        """)

        cursor.execute(update_query, (hashed_password, user_email))
        
        # Commit changes
        conn.commit()

        if cursor.rowcount > 0:
            print(f'Successfully updated password for {user_email}.')
        else:
            print(f'No user found with the email: {user_email}')

    except Exception as e:
        print(f'There was an error: {e}')

    finally:
        # Disconnect from DB
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def main():
    login_or_new_user = int(input('Create a new user (0) or login to an existing account (1)?: '))

    if login_or_new_user == 1:
        # Get login info
        user_email = input('Enter your email address: ')

        if check_email(user_email) == False:
            print('User does not exist!')
            return
        
        user_password = getpass.getpass('Enter your password: ')

        if check_user_password(user_email, user_password) == True:
            print('Thank you for logging in!')
            options = int(input('Do you want to update your password(0), update your email address(1), or delete your account(2)?: '))
            if options == 0:
                new_password = 0
                confirm_password = -1
                while new_password != confirm_password:
                    new_password = getpass.getpass('Enter your new password: ')
                    confirm_password = getpass.getpass('Confirm your new password: ')
                    if new_password != confirm_password:
                        print('Those passwords did not match, please reenter the password.')
                    else:
                        update_user_password(user_email, new_password)
            elif options == 1:
                confirmation_email = 0
                new_email = -1
                while new_email != confirmation_email:
                    new_email = input('What is your new email address?: ')
                    confirmation_email = input('Please confirm your new email address: ')
                    if new_email != confirmation_email:
                        print('The new email addresses did not match, please reenter them.')
                    else:
                        update_user_email(user_email, new_email)
            else:
                confirm = input('Are you sure you want to delete your account?\nOnce you have done this it can NOT be undone.(y,n)')
                if confirm == 'y':
                    delete_user_by_email(user_email)
                    print('Your account has been deleted.')
                    return
                else:
                    print('Thank you for keeping your account!')
        else:
            print('Incorrect username or password')
            return
            
    else:
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        user_email = input('Enter your email address: ')

        user_password = 0
        user_password_confirmed = 1

        while user_password != user_password_confirmed:
            user_password = getpass.getpass('Enter your password: ')
            user_password_confirmed = getpass.getpass('Confirm your password: ')
            if user_password != user_password_confirmed:
                print('Passwords must match!')
        hashed_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
        create_new_user(first_name, last_name, user_email, hashed_password)

if __name__ == '__main__':
    main()