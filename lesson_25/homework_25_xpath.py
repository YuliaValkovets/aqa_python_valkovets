
##[MAIN PAGE]
# //div[@class="col-12 col-lg-6"]/div/div/img
# //nav[@class="header_nav d-flex align-items-center"]/button[last()]
# //div[@class="col-md-6 d-flex flex-column align-items-center align-items-md-start"]/h2[text()="Contacts"]
# //nav[@class="header_nav d-flex align-items-center"]/a[1]
# //div[@class="contacts_socials socials"]/a[last()-1]
# //div[@class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"]/div/p[@class="about-block_title h2"]

##[SIGN UP]
# //form[@class="ng-untouched ng-pristine ng-invalid"]/div[last()-1]/label
# //div[@class="form-group"]/input[@id="signupRepeatPassword"]
# //div[@class="modal-header"]/h4[@class="modal-title" and text()="Registration"]

##[LOG IN form]
# //div[@class="form-group d-flex align-items-center justify-content-between"]/button[@class="btn btn-link"]
# //div[@class="form-check"]/label[text()="Remember me"]
# //div[@class="modal-header"]/button[@class="close"]

##[LOG AS GUEST]
# //nav[@class="sidebar d-flex flex-column"]/a[2]
# //a[@class="btn btn-link text-danger btn-sidebar sidebar_btn" and contains(text(), "Log out")]
# [instructions] = //ul[@class="instructions_list instruction-list"]/li[last()]//a[text()='Download']
# [my profile=>dropdown menu] = //nav[@class="user-nav_menu dropdown-menu show"]/a[text()='Garage']
# //button[@id="userNavDropdown"]/img

##[SIGN IN as user]
# [profile-edit profile] = //div[@class="modal-footer"]/button
# [profile-edit profile] = //button[@class="close"]/span
# [settings] = //div[@class="btn-group"]/button[text()="UAH"]
# [settings] = //div[@class="user-settings_form"]/h2[text()="Remove account"]
# [add a car] = //select[@id="addCarModel"]/option[text()="Q7"]
# [add a car] = //div[@class="form-group"]/label[@for="addCarMileage" and text()="Mileage"
# [add an expense] = //div[@class="modal-footer d-flex justify-content-end"]/button[@class="btn btn-primary"]
# [add an expense] = //div[@class="input-group-append"]/button[@class="btn date-picker-toggle"]