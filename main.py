from Mover import *

if __name__ == '__main__':

    if os.path.exists("mover.pkl"):
        with open("mover.pkl", "rb") as file:
            mover = pickle.load(file)
    else:
        mover = Mover(input("Input your OneDrive folder's name:"), input("Set the password:"))

    mover.update_online_files()

    with open("mover.pkl", "wb") as file:
        pickle.dump(mover, file)