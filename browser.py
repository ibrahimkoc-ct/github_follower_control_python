from selenium import webdriver
import time

class Browser:
     
    def __init__(self,link):
        self.link="https://github.com/"+link
        self.browser=webdriver.Chrome()
        Browser.go_git(self)

    def go_git(self):
        self.browser.get(self.link)
        time.sleep(2)
        follow_info=self.browser.find_elements_by_css_selector(".text-bold.text-gray-dark")
        followers_count=int(follow_info[0].text)
        following_count=int(follow_info[1].text)
        followers_list= Browser.get_followers(self,followers_count)
        time.sleep(2)
        following_list=Browser.get_following(self,following_count)
        list_difference(followers_list,following_list) 
        
    def get_followers(self,followers_count):
        followers_list=[]
        page=page_count(followers_count)
        follow_count=1
        print("******************Followers*************")
        for count in range (1,page+1):
            self.browser.get(self.link+"?page="+str(count)+"&tab=followers")
            time.sleep(1)
            followers=self.browser.find_elements_by_css_selector(".d-inline-block.no-underline.mb-1")
            for follow in followers:
                followers_list.append(follow.get_attribute("href"))
                print(str(follow_count)+". "+follow.get_attribute("href"))
                follow_count +=1
        return followers_list       

     
    def get_following(self,following_count):
        following_list=[]
        page=page_count(following_count)
        follow_count=1
        print("******************Following*************")
        for count in range (1,page+1):
            self.browser.get(self.link+"?page="+str(count)+"&tab=following")
            time.sleep(1)
            followers=self.browser.find_elements_by_css_selector(".d-inline-block.no-underline.mb-1")
            for follow in followers:
                following_list.append(follow.get_attribute("href"))
                print(str(follow_count)+". "+follow.get_attribute("href"))
                follow_count +=1 
        return following_list          




def page_count(count):
        page=count/50
        if(count%50==0):
            page=int(count/50)
        else:
              page=int(count/50+1)
        return page  

def list_difference(followers_list,following_list):
    unfollowers=set(following_list)-set(followers_list)
    count=1
    print("************Unfollowers**************")
    for unfollower in unfollowers:
        print(str(count)+". "+unfollower)
        count+=1
    count=1    
    print("**********Unfollowing**************")
    unfollowing=set(followers_list)-set(following_list)
    for unfollow in unfollowing:
        print(str(count)+". "+unfollow)
        count+=1 
     
