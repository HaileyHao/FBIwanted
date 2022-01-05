# FBIwanted

This package is a [FBI Wanted API](https://www.fbi.gov/wanted/api) python wrapper. 

It allows you to retrieve a data set of FBI wanted people by their appearance features or by administrative regions(city name), as well as downloading their posters to see the photos.       

Try it out if you suspect someone you see may be a FBI wanted person, with the data set retrieved with this package, you may find out whether you are in real danger and whether there is a reward!


## Installation 

```bash
$ pip install -i https://test.pypi.org/simple/ fbiwanted
```

## Usage

### Functions

#### 1. fbi_wanted_appearance

`fbi_wanted_appearance(eyes = None, hair = None, race = None)`

Retrieve a data set of FBI wanted people by appearance features, including eye color, hair color and race.

#### 2. fbi_wanted_office

`fbi_wanted_office(field_offices = None)`

Retrieve a data set of FBI wanted people by administration office. Input a lowercase city name with no space.

#### 3. fbi_poster_appearance

`fbi_poster_appearance(eyes = None, hair = None, race = None)`

Download the posters of the FBI wanted people who look as you described. Easy way to compare and find out if you have really met a fugitive or missing person.


## Column description

There are 12 columns in the dataframe you get using this package, with the function fbi_wanted_appearance() and fbi_wanted_office() below.

They are:
#### - name
#### - status: 
Whether the FBI wanted person has been captured. "captured" means they've been captured, na means they are still out there. 
#### - sex
#### - nationality
#### - race
#### - hair: 
Hair color of the FBI wanted person when last seen, "bald" means they had no hair.
#### - eyes: 
Eye color of the FBI wanted person.
#### - height_max: 
The estimated maximum height, in inches.
#### - height_min: 
The estimated minimum height, in inches.
#### - scars_and_marks: 
Descriptions of the scars or marks the FBI wanted person has on their body.
#### - dates_of_birth_used
#### - place_of_birth
#### - occupations
#### - languages
#### - aliases
#### - subjects: 
The catrgory of the reason why the FBI wanted person is wanted, like "White-Collar Crime“, "Kidnappings and Missing Persons", etc.
#### - field_offices: 
A lowercase city name with no space between words. 
#### - url: 
A url that leads to the FBI webpage of the FBI wanted person. **Photos**, posters, and more details may be found there.
#### - reward_max: 
The amount of reward one may get by providing clues for finding the FBI wanted person.
#### - warning_message: 
A warning message indicating whether the FBI wanted person is armed, or be dangerous in other ways.

(More columns may be included in the future releases of this package.)



## Quick Start


### import all functions

`>>> from fbiwanted import FBIwanted`

### 1. Retrieve FBI wanted people info by appearance.

#### Example: Look for information of FBI wanted people with brown eyes, blond hair and are white.

`>>> FBIwanted.fbi_wanted_appearance(eyes = "brown", hair = "blond", race = "white")`

It returns a message telling you how many records are found, and a pandas dataframe with 12 columns.

> 12 records retrieved.

More about the input and out can be found with the help() function.

`>>> help(fbi_wanted_appearance)` 

<!-- |    | name                         | status   | sex    | nationality   | race   | hair   | eyes   |   height_max |   height_min | scars_and_marks                                                                                                               | dates_of_birth_used   | place_of_birth             | occupations                                                                                  | languages   | aliases                      | subjects                   | field_offices   | url                                                                |   reward_max | warning_message                                                                            |
|---:|:-----------------------------|:---------|:-------|:--------------|:-------|:-------|:-------|-------------:|-------------:|:------------------------------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------|:---------------------------------------------------------------------------------------------|:------------|:-----------------------------|:---------------------------|:----------------|:-------------------------------------------------------------------|-------------:|:-------------------------------------------------------------------------------------------|
|  0 | Laura Ann Johnson            | na       | Female |               | white  | blond  | brown  |           66 |           66 | Surgery scar on left forearm                                                                                                  |                       |                            | Officer in the Russian Federation’s Main Intelligence Directorate of the General Staff (GRU) |             | Лукашев Алексей Викторович   | ViCAP Missing Persons      | washingtondc    | https://www.fbi.gov/wanted/vicap/missing-persons/laura-ann-johnson |            0 |                                                                                            |
|    |                              |          |        |               |        |        |        |              |              | Sunburst and bird on right arm                                                                                                |                       |                            |                                                                                              |             |                              |                            |                 |                                                                    |              |                                                                                            |
|    |                              |          |        |               |        |        |        |              |              | Scroll and lady bug on left breast                                                                                            |                       |                            |                                                                                              |             |                              |                            |                 |                                                                    |              |                                                                                            |
|    |                              |          |        |               |        |        |        |              |              | Red rose on abdomen                                                                                                           |                       |                            |                                                                                              |             |                              |                            |                 |                                                                    |              |                                                                                            |
|    |                              |          |        |               |        |        |        |              |              | Roses on right ankle                                                                                                          |                       |                            |                                                                                              |             |                              |                            |                 |                                                                    |              |                                                                                            |
|  1 | Debra Kay King               | na       | Female |               | white  | blond  | brown  |           64 |           64 | King has a scar on her abdomen and an unknown tattoo on her left hand.                                                        |                       |                            | Officer in the Russian Federation's Main Intelligence Directorate of the General Staff (GRU) |             | Anna V.                      | ViCAP Missing Persons      | minneapolis     | https://www.fbi.gov/wanted/vicap/missing-persons/debra-kay-king    |            0 |                                                                                            |
|  2 | Simone S. Ridinger           | na       | Female |               | white  | blond  | brown  |           63 |           62 | Ridinger has a birthmark on her lower back and a small mole on her upper right forehead.                                      |                       |                            | Officer in the Russian Federation's Main Intelligence Directorate of the General Staff (GRU) |             | "Tammy"                      | ViCAP Missing Persons      | pittsburgh      | https://www.fbi.gov/wanted/vicap/missing-persons/simone-s-ridinger |            0 |                                                                                            |
|  3 | Aleksey Viktorovich Lukashev | na       | Male   | Russian       | white  | blond  | brown  |          nan |          nan |                                                                                                                               | ['November 7, 1990']  | Murmanskaya Oblast, Russia | nan                                                                                          |             | Сергей Владимирович Детистов | Cyber's Most Wanted        | losangeles      | https://www.fbi.gov/wanted/cyber/aleksey-viktorovich-lukashev      |            0 | SHOULD BE CONSIDERED ARMED AND DANGEROUS, AN INTERNATIONAL FLIGHT RISK, AND AN ESCAPE RISK |
|  4 | Jane Doe                     | na       | Female |               | white  | blond  | brown  |           64 |           64 | Moles on the left side of the forehead, tip of the right shoulder, left clavicle,  front of the right lower leg,  right ankle |                       |                            | nan                                                                                          |             | Павел Валерьевич Фролов      | ViCAP Unidentified Persons | newark          | https://www.fbi.gov/wanted/vicap/unidentified-persons/jane-doe-6   |            0 |                                                                                            |
|    |                              |          |        |               |        |        |        |              |              | Old scars are noted on the back of the left hand, below the right knee, and on the back of the right forearm                  |                       |                            |                                                                                              |             |                              |                            |                 |                                                                    |              |                                                                                            | -->



### 2. Retrieve FBI wanted people info by city name.

#### Example: Look for information of FBI wanted people under the adminiatration of FBI office in Honolulu.

`>>> FBIwanted.fbi_wanted_office(field_offices = "honolulu"))`

It also returns a message telling you how many records are found, and a pandas dataframe, with the same 12 columns as function 1:

> 5 records retrieved.

More about the input and out can be found with the help() function.

`>>> help(fbi_wanted_office)` 

<!-- 
|    | name                         | status   | sex    | nationality   | race   | hair   | eyes   |   height_max |   height_min | scars_and_marks                                   | dates_of_birth_used   | place_of_birth                           | occupations   | languages            | aliases                                                                        | subjects                        | field_offices   | url                                                           |   reward_max | warning_message                          |
|---:|:-----------------------------|:---------|:-------|:--------------|:-------|:-------|:-------|-------------:|-------------:|:--------------------------------------------------|:----------------------|:-----------------------------------------|:--------------|:---------------------|:-------------------------------------------------------------------------------|:--------------------------------|:----------------|:--------------------------------------------------------------|-------------:|:-----------------------------------------|
|  0 | Julieanne Baldueza Dimitrion | na       | Female | American      | asian  | black  | brown  |           59 |           59 | None known                                        | ['March 22, 1972']    | Massachusetts                            | ['Unknown']   |                      | ['Julie Anne Baldueza Dimitrion']                                              | White-Collar Crime              | honolulu        | https://www.fbi.gov/wanted/wcc/julieanne-baldueza-dimitrion   |        10000 |                                          |
|  1 | John Michael Dimitrion       | na       | Male   | American      |        | black  | brown  |           67 |           67 | None known                                        | ['April 12, 1976']    | Hawaii                                   | ['Unknown']   |                      | ['John M. Dimitrion', 'John Dela Cruz']                                        | White-Collar Crime              | honolulu        | https://www.fbi.gov/wanted/wcc/john-michael-dimitrion         |        10000 |                                          |
|  2 | Maleina Luhk                 | na       | Female | American      | asian  | brown  | brown  |           48 |           48 | Maleina has a birthmark on her left cheek.        | ['February 13, 2002'] | Saipan, Northern Mariana Islands         |               |                      |                                                                                | Kidnappings and Missing Persons | honolulu        | https://www.fbi.gov/wanted/kidnap/maleina-luhk                |            0 |                                          |
|  3 | Faloma Luhk                  | na       | Female | American      | asian  | brown  | brown  |           61 |           61 |                                                   | ['February 9, 2001']  | Saipan, Northern Mariana Islands         |               |                      |                                                                                | Kidnappings and Missing Persons | honolulu        | https://www.fbi.gov/wanted/kidnap/faloma-luhk                 |            0 |                                          |
|  4 | Raddulan Sahiron             | na       | Male   | Filipino      | asian  | gray   | black  |           66 |           66 | Sahiron's right arm is amputated above his elbow. |                       | Kabbun Takas, Patikul, Jolo, Philippines |               | ['Tausug', 'Arabic'] | ['Radullan Sahiron', 'Radulan Sahiron', 'Raddulan Sahirun', 'Commander Putol'] | Most Wanted Terrorists          | honolulu        | https://www.fbi.gov/wanted/wanted_terrorists/raddulan-sahiron |            0 | SHOULD BE CONSIDERED ARMED AND DANGEROUS |
 -->


### 3. Download posters of FBI wanted people by appearence.

#### Example: Download posters of FBI wanted people with black eyes and black hair.

`>>> FBIwanted.fbi_poster_appearance(eyes = "black", hair = "black")`

It returns a message telling you how many poster PDFs are downloaded.

> Download completed. 10 posters downloaded.

**Posters in PDF format will be downloaded into your working directory. Careful! There can be hundreds of posters.**

## Try it out

- Here is a [jupyter notebook demo](https://github.com/QMSS-G5072-2021/Hao_Qinyue/blob/main/Final_Project/FBIwanted/demo/Demo.ipynb) with the example codes above, just change the parameters to get the data set you want! Note that I've already ran the sample codes once, so there are some poster PDF files in the Demo folder.

- Here you can retrieve and explore the [whole original dataset](https://github.com/QMSS-G5072-2021/Hao_Qinyue/blob/main/Final_Project/FBIwanted/demo/Whole_Original_Dataset.ipynb). A function to retrieve a complete and clean full dataset will also be added in future releases.



## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`FBIwanted` was created by Qinyue Hao. It is licensed under the terms of the MIT license.

## Credits

`FBIwanted` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
