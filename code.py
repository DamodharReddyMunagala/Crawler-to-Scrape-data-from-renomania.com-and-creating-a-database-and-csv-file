# WebCrawler-to-Scrape-data-from-https-renomania.com-pro-professionals-home-professionals-
import requests
from bs4 import BeautifulSoup
import pymongo
import re
import urllib.request as UrlRequest
from urllib.request import urlopen
import pandas as pd
from pymongo import MongoClient
from pymongo import MongoClient as Connection

#for pages method
pageUrls = []
firmPage = []
firmCompany = []

#for firmProfile method
firmWebsite = []
firmPhone = []
firmPrimaryCategory = []
firmSecondaryCategory = []
firmServicesProvided = []
firmMobile = []
firmContactName = []
firmAddress = []
firmMinimumJobCostInINR = []
firmDescription = []
firmProjectsPageLink = []

#for firmProjectsGalleryPageLink method
firmImage = []
projectImageTitleList = []
projectImageUrlList = []
projectGalleryImagesUrlsList = []
        
def pages(url):
    """
    try:
        BeautifulSoup(open(url.replace('https://','').replace('.','-').replace('/','-') + '.html'), 'lxml')
    except FileNotFoundError:
        req = requests.get(url)
        req.raise_for_status()
        response = open(url.replace('https://','').replace('.','-').replace('/','-') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            response.write(chunk)
        response.close()
    """
    
    soup = BeautifulSoup(open(url.replace('https://','').replace('.','-').replace('/','-') + '.html'), 'lxml')
    
    try:
        for data in soup.findAll('div', {'class' : 'col-xs-6 prologobgsml'}):
            if 'https://renomania.com' + data.find('a').attrs['href'] in firmPage:
                pass
            else:
                firmPage.append('https://renomania.com' + data.find('a').attrs['href'])
    except AttributeError:
        firmPage.append('None')
    
    for data in soup.findAll('div', {'class' : 'media-body profileinfo'}):
        for item in data.find('h4').findAll('a', href = re.compile('^(/pro/profile/)')):
            firmCompany.append(item.text)


def firmProfile(firmPage):
    """
    try:
        BeautifulSoup(open(firmPage.replace('/', '').replace('.', '') + '.html'), 'lxml')
    except FileNotFoundError:
        req = requests.get(firmPage, verify = False)
        response = open(firmPage.replace('/', '').replace('.', '') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            response.write(chunk)
        response.close()
    """
    soup = BeautifulSoup(open(firmPage.replace('/', '').replace('.', '') + '.html'), 'lxml')
    
    
    for data in soup.find('div', {'class' : 'col-md-11 contentrtbg spaceupdown'}).find('div', {'class' : 'col-md-4'}).findAll('ul'):
        cells = []
        cells = data.findAll('li')
        try:
            if 'Website:' in cells[0].text:
                firmWebsite.append(cells[0].find('a').attrs['href'])
            elif 'Website:' in cells[1].text:
                firmWebsite.append(cells[1].find('a').attrs['href'])
            elif 'Website:' in cells[2].text:
                firmWebsite.append(cells[2].find('a').attrs['href'])
            elif 'Website:' in cells[3].text:
                firmWebsite.append(cells[3].find('a').attrs['href'])
            elif 'Website:' in cells[4].text:
                firmWebsite.append(cells[4].find('a').attrs['href'])
            elif 'Website:' in cells[5].text:
                firmWebsite.append(cells[5].find('a').attrs['href'])
            elif 'Website:' in cells[6].text:
                firmWebsite.append(cells[6].find('a').attrs['href'])
            elif 'Website:' in cells[7].text:
                firmWebsite.append(cells[7].find('a').attrs['href'])
            elif 'Website:' in cells[8].text:
                firmWebsite.append(cells[8].find('a').attrs['href'])
            else:
                firmWebsite.append('')
        except IndexError:
                firmWebsite.append('')
        except AttributeError:
            firmWebsite.append('')

        try:
            if 'Phone:' in cells[0].text:
                firmPhone.append(cells[0].span.text)
            elif 'Phone:' in cells[1].text:
                firmPhone.append(cells[1].span.text)
            elif 'Phone:' in cells[2].text:
                firmPhone.append(cells[2].span.text)
            elif 'Phone:' in cells[3].text:
                firmPhone.append(cells[3].span.text)
            elif 'Phone:' in cells[4].text:
                firmPhone.append(cells[4].span.text)
            elif 'Phone:' in cells[5].text:
                firmPhone.append(cells[5].span.text)
            elif 'Phone:' in cells[6].text:
                firmPhone.append(cells[6].span.text)
            elif 'Phone:' in cells[7].text:
                firmPhone.append(cells[7].span.text)
            elif 'Phone:' in cells[8].text:
                firmPhone.append(cells[8].span.text)
            else:
                firmPhone.append('')
        except AttributeError:
            firmPhone.append('')
        except IndexError:
            firmPhone.append('')

        try:
            if 'Primary Category:' in cells[0].text:
                firmPrimaryCategory.append(cells[0].span.text)
            elif 'Primary Category:' in cells[1].text:
                firmPrimaryCategory.append(cells[1].span.text)
            elif 'Primary Category:' in cells[2].text:
                firmPrimaryCategory.append(cells[2].span.text)
            elif 'Primary Category:' in cells[3].text:
                firmPrimaryCategory.append(cells[3].span.text)
            elif 'Primary Category:' in cells[4].text:
                firmPrimaryCategory.append(cells[4].span.text)
            elif 'Primary Category:' in cells[5].text:
                firmPrimaryCategory.append(cells[5].span.text)
            elif 'Primary Category:' in cells[6].text:
                firmPrimaryCategory.append(cells[6].span.text)
            elif 'Primary Category:' in cells[7].text:
                firmPrimaryCategory.append(cells[7].span.text)
            elif 'Primary Category:' in cells[8].text:
                firmPrimaryCategory.append(cells[8].span.text)
        except IndexError:
            firmPrimaryCategory.append('')
        except AttributeError:
            firmPrimaryCategory.append('')

        try:
            if 'Secondary Category:' in cells[0].text:
                firmSecondaryCategory.append(cells[0].span.text)
            elif 'Secondary Category:' in cells[1].text:
                firmSecondaryCategory.append(cells[1].span.text)
            elif 'Secondary Category:' in cells[2].text:
                firmSecondaryCategory.append(cells[2].span.text)
            elif 'Secondary Category:' in cells[3].text:
                firmSecondaryCategory.append(cells[3].span.text)
            elif 'Secondary Category:' in cells[4].text:
                firmSecondaryCategory.append(cells[4].span.text)
            elif 'Secondary Category:' in cells[5].text:
                firmSecondaryCategory.append(cells[5].span.text)
            elif 'Secondary Category:' in cells[6].text:
                firmSecondaryCategory.append(cells[6].span.text)
            elif 'Secondary Category:' in cells[7].text:
                firmSecondaryCategory.append(cells[7].span.text)
            elif 'Secondary Category:' in cells[8].text:
                firmSecondaryCategory.append(cells[8].span.text)
        except IndexError:
            firmSecondaryCategory.append('')
        except AttributeError:
            firmSecondaryCategory.append('')

        try:
            if 'Services Provided:' in cells[0].text:
                firmServicesProvided.append(cells[0].span.text)
            elif 'Services Provided:' in cells[1].text:
                firmServicesProvided.append(cells[1].span.text)
            elif 'Services Provided:' in cells[2].text:
                firmServicesProvided.append(cells[2].span.text)
            elif 'Services Provided:' in cells[3].text:
                firmServicesProvided.append(cells[3].span.text)
            elif 'Services Provided:' in cells[4].text:
                firmServicesProvided.append(cells[4].span.text)
            elif 'Services Provided:' in cells[5].text:
                firmServicesProvided.append(cells[5].span.text)
            elif 'Services Provided:' in cells[6].text:
                firmServicesProvided.append(cells[6].span.text)
            elif 'Services Provided:' in cells[7].text:
                firmServicesProvided.append(cells[7].span.text)
            elif 'Services Provided:' in cells[8].text:
                firmServicesProvided.append(cells[8].span.text)
        except IndexError:
            firmServicesProvided.append('')
        except AttributeError:
            firmServicesProvided.append('')

        try:
            if 'Mobile:' in cells[0].text:
                firmMobile.append(cells[0].span.text)
            elif 'Mobile:' in cells[1].text:
                firmMobile.append(cells[1].span.text)
            elif 'Mobile:' in cells[2].text:
                firmMobile.append(cells[2].span.text)
            elif 'Mobile:' in cells[3].text:
                firmMobile.append(cells[3].span.text)
            elif 'Mobile:' in cells[4].text:
                firmMobile.append(cells[4].span.text)
            elif 'Mobile:' in cells[5].text:
                firmMobile.append(cells[5].span.text)
            elif 'Mobile:' in cells[6].text:
                firmMobile.append(cells[6].span.text)
            elif 'Mobile:' in cells[7].text:
                firmMobile.append(cells[7].span.text)
            elif 'Mobile:' in cells[8].text:
                firmMobile.append(cells[8].span.text)
        except IndexError:
            firmMobile.append('')
        except AttributeError:
            firmMobile.append('')

        try:
            if 'Contact Name:' in cells[0].text:
                firmContactName.append(cells[0].span.text)
            elif 'Contact Name:' in cells[1].text:
                firmContactName.append(cells[1].span.text)
            elif 'Contact Name:' in cells[2].text:
                firmContactName.append(cells[2].span.text)
            elif 'Contact Name:' in cells[3].text:
                firmContactName.append(cells[3].span.text)
            elif 'Contact Name:' in cells[4].text:
                firmContactName.append(cells[4].span.text)
            elif 'Contact Name:' in cells[5].text:
                firmContactName.append(cells[5].span.text)
            elif 'Contact Name:' in cells[6].text:
                firmContactName.append(cells[6].span.text)
            elif 'Contact Name:' in cells[7].text:
                firmContactName.append(cells[7].span.text)
            elif 'Contact Name:' in cells[8].text:
                firmContactName.append(cells[8].span.text)
        except IndexError:
            firmContactName.append('')
        except AttributeError:
            firmContactName.append('')

        try:
            if 'Address:' in cells[0].text:
                firmAddress.append(cells[0].span.text)
            elif 'Address:' in cells[1].text:
                firmAddress.append(cells[1].span.text)
            elif 'Address:' in cells[2].text:
                firmAddress.append(cells[2].span.text)
            elif 'Address:' in cells[3].text:
                firmAddress.append(cells[3].span.text)
            elif 'Address:' in cells[4].text:
                firmAddress.append(cells[4].span.text)
            elif 'Address:' in cells[5].text:
                firmAddress.append(cells[5].span.text)
            elif 'Address:' in cells[6].text:
                firmAddress.append(cells[6].span.text)
            elif 'Address:' in cells[7].text:
                firmAddress.append(cells[7].span.text)
            elif 'Address:' in cells[8].text:
                firmAddress.append(cells[8].span.text)
        except IndexError:
            firmAddress.append('')
        except AttributeError:
            firmAddress.append('')

        try:
            if 'Minimum job cost in INR:' in cells[0].text:
                firmMinimumJobCostInINR.append(cells[0].span.text)
            elif 'Minimum job cost in INR:' in cells[1].text:
                firmMinimumJobCostInINR.append(cells[1].span.text)
            elif 'Minimum job cost in INR:' in cells[2].text:
                firmMinimumJobCostInINR.append(cells[2].span.text)
            elif 'Minimum job cost in INR:' in cells[3].text:
                firmMinimumJobCostInINR.append(cells[3].span.text)
            elif 'Minimum job cost in INR:' in cells[4].text:
                firmMinimumJobCostInINR.append(cells[4].span.text)
            elif 'Minimum job cost in INR:' in cells[5].text:
                firmMinimumJobCostInINR.append(cells[5].span.text)
            elif 'Minimum job cost in INR:' in cells[6].text:
                firmMinimumJobCostInINR.append(cells[6].span.text)
            elif 'Minimum job cost in INR:' in cells[7].text:
                firmMinimumJobCostInINR.append(cells[7].span.text)
            elif 'Minimum job cost in INR:' in cells[8].text:
                firmMinimumJobCostInINR.append(cells[8].span.text)
        except IndexError:
            firmMinimumJobCostInINR.append('')
        except AttributeError:
            firmMinimumJobCostInINR.append('')
    try:
        for data in soup.find('div', {'class' : 'col-md-11 contentrtbg spaceupdown'}).find('div', {'class' : 'col-md-8'}).findAll('p', {'class' : 'comment1'}):
            firmDescription.append(data.text.replace('\t', '').replace('\n', ''))
    except AttributeError:
        firmDescription.append('')
    
    try:
        projectLink = soup.find('a', href = re.compile('^(/pro/projects/)'))
        firmProjectsPageLink.append('https://renomania.com' + projectLink.attrs['href'])
    except AttributeError:
        firmProjectsPageLink.append('')

def firmProjectsGalleryPageLink(firmProjectsPageLink):
    projectImageGalleryLink = []
    projectImageUrl = []
    projectImageTitle = []
    projectGalleryImagesUrls = []
    """
    try:
        BeautifulSoup(open(firmProjectsPageLink.replace('.', '').replace('/', '') + '.html'), 'lxml')
    except FileNotFoundError:
        req = requests.get(firmProjectsPageLink, verify = False)
        response = open(firmProjectsPageLink.replace('.', '').replace('/', '') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            response.write(chunk)
        response.close()
    """
    soup = BeautifulSoup(open(firmProjectsPageLink.replace('.', '').replace('/', '') + '.html'), 'lxml')

    for data in soup.findAll('div', {'class' : 'profile-userpic'}):
        if 'https:' not in data.find('img').attrs['src']:
            firmImage.append('https:' + data.find('img').attrs['src'])
        else:
            firmImage.append(data.find('img').attrs['src'])

    for data in soup.find('div', {'id' : 'project_list'}).findAll('div', {'class' : 'col-md-4'}):
        projectImageGalleryLink.append('https://renomania.com' + data.find('a').attrs['href'])
        try:
            for item in data.find('a').findAll('div', {'class' : 'imgcropthree'}):
                projectImageTitle.append(item.attrs['title'])
                projectImageUrl.append(item.attrs['style'].replace('background-image:url(', '').replace(')', '').replace(';', ''))
        except AttributeError:
            projectImageTitle.append('')
            projectImageUrl.append('')
    projectImageTitleList.append(projectImageTitle)
    projectImageUrlList.append(projectImageUrl)
    
    for link in projectImageGalleryLink:
        projectGalleryImagesUrls.append(ImageGallery(link))
    
    projectGalleryImagesUrlsList.append(projectGalleryImagesUrls)

def ImageGallery(projectImageGalleryLink):
    ImageUrl = []
    ImageUrlList = []
    """
    try:
        BeautifulSoup(open(projectImageGalleryLink.replace('.', '').replace('/', '') + '.html'), 'lxml')
    except FileNotFoundError:
        req = requests.get(projectImageGalleryLink, verify = False)
        response = open(projectImageGalleryLink.replace('.', '').replace('/', '') + '.html', 'wb')
        for chunk in req.iter_content(100000):
            response.write(chunk)
        response.close()
    """
    soup = BeautifulSoup(open(projectImageGalleryLink.replace('.', '').replace('/', '') + '.html'), 'lxml')

    for data in soup.find('div', {'id' : 'project_list'}).findAll('div', {'class' : 'col-md-6'}):
        for item in data.find('a').findAll('div', {'class' : 'imgcropthree'}):
            ImageUrl.append(item.attrs['style'].replace('background-image: url(', '').replace(')', '').replace(';', ''))
            
    for i in range(len(ImageUrl)):
        ImageUrlList.append(ImageUrl[i])
    
    return (ImageUrlList)


for i in range(1, 75):
    url = 'https://renomania.com/pro/professionals/home-professionals' + '/p/' + str(i)
    pages(url)

for link in firmPage:
    firmProfile(link)

for link in firmProjectsPageLink:
    firmProjectsGalleryPageLink(link)


connection = Connection()
db = connection.hutstoryRenomania
firmCollection = db.firms
projectCollection = db.projects
imageGalleryCollection = db.images
for i in range(len(firmPage)):
    insertFirmData = {"CompanyName" : firmCompany[i],
                     "FirmImage" : firmImage[i],
                     "PrimaryCategory" : firmPrimaryCategory[i],
                     "SecondaryCategory" : firmSecondaryCategory[i],
                     "ServicesProvided" : firmServicesProvided[i],
                     "Website" : firmWebsite[i],
                     "PhoneNumber" : firmPhone[i],
                     "MobileNumber" : firmMobile[i],
                     "ContactName" : firmContactName[i],
                     "Address" : firmAddress[i],
                     "Description" : firmDescription[i],
                     "FirmPage" : firmPage[i]}
    FIRMID = firmCollection.insert_one(insertFirmData).inserted_id
    
    for j in range(len(projectImageTitleList[i])):
        insertProjectData = {"ProjectImageTitle" : projectImageTitleList[i][j],
                            "ProjectImageUrl" : projectImageUrlList[i][j],
                            "firmId" : FIRMID}
        PROJECTID = projectCollection.insert_one(insertProjectData).inserted_id
        
        for k in range(len(projectGalleryImagesUrlsList[i][j])):
            insertImageData = {"ImagesOfProjectsUrl" : projectGalleryImagesUrlsList[i][j][k],
                              "projectId" : PROJECTID}
            IMAGEID = imageGalleryCollection.insert_one(insertImageData).inserted_id

#Creating a DataFrame
df=pd.DataFrame(firmCompany,columns=['Company Name'])
df['Contact Name']=firmContactName
df['Firm Image']=firmImage
df['Address'] = firmAddress
df['Website Address'] = firmWebsite
df['Mobile Number'] = firmMobile
df['Phone Number'] = firmPhone
df['Services Provided'] = firmServicesProvided
df['Primary Category'] = firmPrimaryCategory
df['SecondaryCategory'] = firmSecondaryCategory
df['Firm Page'] = firmPage
df['Description'] = firmDescription
df['Project Image Title'] = projectImageTitleList
df['Project Image Url'] = projectImageUrlList
df['Image Gallery of Project Urls'] = projectGalleryImagesUrlsList
df.to_csv('01234Renomania.csv',index=True,header=True)
