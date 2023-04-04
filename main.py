import spring as clean
import hw 
import call_api
def main():
    content = 'test.txt'
    clean.spaced(content)
    clean.clean_list(content)
    hw.make_task(content)
    call_api.call()


if __name__ == "__main__":
    main()
    
