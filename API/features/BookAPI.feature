# Created by Rupesh at 06-07-2021
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then Book is successfully added

   @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle> which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then Book is successfully added
    Examples:
      | isbn  | aisle |
      | India | 1508  |
      | US    | 1401  |
      | UK    | 1202  |
