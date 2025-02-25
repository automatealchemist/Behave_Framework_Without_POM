Feature: OramgeHRM Login


  Background :
    Given Openhrm Page is open


  Scenario: OrangeHRM Login
    When enter username "admin" and password "admin123"
    Then user must be successfully login into the system
    And close browser

  Scenario Outline: OrangeHRM Login with Multiple parameters

    When enter username "<username>" and password "<password>"
    Then user must be successfully login into the system
    And close browser

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
