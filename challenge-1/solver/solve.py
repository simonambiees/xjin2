
def main():
    flag = "joe_biden_is_our_comrade_6ffac749573f71f3"
    flag = flag.strip()
    with open('./flag', 'w') as w:
        w.write(flag)

if __name__ == "__main__":
    main()