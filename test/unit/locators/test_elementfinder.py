import unittest
import os
from Selenium2Library.locators import ElementFinder
from mockito import *

class ElementFinderTests(unittest.TestCase):

    def test_find_with_invalid_prefix(self):
        finder = ElementFinder()
        browser = mock()
        with self.assertRaises(ValueError) as context:
            finder.find(browser, "something=test1")
        self.assertEqual(context.exception.message, "Element locator with prefix 'something' is not supported")

    def test_find_with_null_browser(self):
        finder = ElementFinder()
        with self.assertRaises(AssertionError):
            finder.find(None, "id=test1")

    def test_find_with_null_locator(self):
        finder = ElementFinder()
        browser = mock()
        with self.assertRaises(AssertionError):
            finder.find(browser, None)

    def test_find_with_empty_locator(self):
        finder = ElementFinder()
        browser = mock()
        with self.assertRaises(AssertionError):
            finder.find(browser, "")

    def test_find_with_no_tag(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test1")
        verify(browser).find_elements_by_xpath("//*[(@id='test1' or @name='test1')]")

    def test_find_with_tag(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test1", tag='div')
        verify(browser).find_elements_by_xpath("//div[(@id='test1' or @name='test1')]")

    def test_find_with_locator_with_apos(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test '1'")
        verify(browser).find_elements_by_xpath("//*[(@id=\"test '1'\" or @name=\"test '1'\")]")

    def test_find_with_locator_with_quote(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test \"1\"")
        verify(browser).find_elements_by_xpath("//*[(@id='test \"1\"' or @name='test \"1\"')]")

    def test_find_with_locator_with_quote_and_apos(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test \"1\" and '2'")
        verify(browser).find_elements_by_xpath(
            "//*[(@id=concat('test \"1\" and ', \"'\", '2', \"'\", '') or @name=concat('test \"1\" and ', \"'\", '2', \"'\", ''))]")

    def test_find_with_a(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='a')
        verify(browser).find_elements_by_xpath(
            "//a[(@id='test1' or @name='test1' or @href='test1' or normalize-space(descendant-or-self::text())='test1' or @href='http://localhost/test1')]")

    def test_find_with_link_synonym(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='link')
        verify(browser).find_elements_by_xpath(
            "//a[(@id='test1' or @name='test1' or @href='test1' or normalize-space(descendant-or-self::text())='test1' or @href='http://localhost/test1')]")

    def test_find_with_img(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='img')
        verify(browser).find_elements_by_xpath(
            "//img[(@id='test1' or @name='test1' or @src='test1' or @alt='test1' or @src='http://localhost/test1')]")

    def test_find_with_image_synonym(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='image')
        verify(browser).find_elements_by_xpath(
            "//img[(@id='test1' or @name='test1' or @src='test1' or @alt='test1' or @src='http://localhost/test1')]")

    def test_find_with_input(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='input')
        verify(browser).find_elements_by_xpath(
            "//input[(@id='test1' or @name='test1' or @value='test1' or @src='test1' or @src='http://localhost/test1')]")

    def test_find_with_radio_button_synonym(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='radio button')
        verify(browser).find_elements_by_xpath(
            "//input[@type='radio' and (@id='test1' or @name='test1' or @value='test1' or @src='test1' or @src='http://localhost/test1')]")

    def test_find_with_checkbox_synonym(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='checkbox')
        verify(browser).find_elements_by_xpath(
            "//input[@type='checkbox' and (@id='test1' or @name='test1' or @value='test1' or @src='test1' or @src='http://localhost/test1')]")

    def test_find_with_file_upload_synonym(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='file upload')
        verify(browser).find_elements_by_xpath(
            "//input[@type='file' and (@id='test1' or @name='test1' or @value='test1' or @src='test1' or @src='http://localhost/test1')]")

    def test_find_with_text_field_synonym(self):
        finder = ElementFinder()
        browser = mock()
        when(browser).get_current_url().thenReturn("http://localhost/mypage.html")
        finder.find(browser, "test1", tag='text field')
        verify(browser).find_elements_by_xpath(
            "//input[@type='text' and (@id='test1' or @name='test1' or @value='test1' or @src='test1' or @src='http://localhost/test1')]")

    def test_find_with_button(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test1", tag='button')
        verify(browser).find_elements_by_xpath(
            "//button[(@id='test1' or @name='test1' or @value='test1' or normalize-space(descendant-or-self::text())='test1')]")

    def test_find_with_select(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test1", tag='select')
        verify(browser).find_elements_by_xpath(
            "//select[(@id='test1' or @name='test1')]")

    def test_find_with_list_synonym(self):
        finder = ElementFinder()
        browser = mock()
        finder.find(browser, "test1", tag='list')
        verify(browser).find_elements_by_xpath(
            "//select[(@id='test1' or @name='test1')]")

    def test_find_with_implicit_xpath(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_xpath("//*[(@test='1')]").thenReturn(elements)

        result = finder.find(browser, "//*[(@test='1')]")
        self.assertEqual(result, elements)
        result = finder.find(browser, "//*[(@test='1')]", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_identifier(self):
        finder = ElementFinder()
        browser = mock()

        id_elements = self._make_mock_elements('div', 'a')
        name_elements = self._make_mock_elements('span', 'a')
        when(browser).find_elements_by_id("test1").thenReturn(list(id_elements)).thenReturn(list(id_elements))
        when(browser).find_elements_by_name("test1").thenReturn(list(name_elements)).thenReturn(list(name_elements))

        all_elements = list(id_elements)
        all_elements.extend(name_elements)

        result = finder.find(browser, "identifier=test1")
        self.assertEqual(result, all_elements)
        result = finder.find(browser, "identifier=test1", tag='a')
        self.assertEqual(result, [id_elements[1], name_elements[1]])

    def test_find_by_id(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_id("test1").thenReturn(elements)

        result = finder.find(browser, "id=test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "id=test1", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_name(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_name("test1").thenReturn(elements)

        result = finder.find(browser, "name=test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "name=test1", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_xpath(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_xpath("//*[(@test='1')]").thenReturn(elements)

        result = finder.find(browser, "xpath=//*[(@test='1')]")
        self.assertEqual(result, elements)
        result = finder.find(browser, "xpath=//*[(@test='1')]", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_dom(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).execute_script("return document.getElementsByTagName('a');").thenReturn(
            [elements[1], elements[3]])

        result = finder.find(browser, "dom=document.getElementsByTagName('a')")
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_link_text(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_link_text("my link").thenReturn(elements)

        result = finder.find(browser, "link=my link")
        self.assertEqual(result, elements)
        result = finder.find(browser, "link=my link", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_css_selector(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_css_selector("#test1").thenReturn(elements)

        result = finder.find(browser, "css=#test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "css=#test1", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_by_tag_name(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_tag_name("div").thenReturn(elements)

        result = finder.find(browser, "tag=div")
        self.assertEqual(result, elements)
        result = finder.find(browser, "tag=div", tag='a')
        self.assertEqual(result, [elements[1], elements[3]])

    def test_find_with_sloppy_prefix(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_id("test1").thenReturn(elements)

        result = finder.find(browser, "ID=test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "iD=test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "id=test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "  id =test1")
        self.assertEqual(result, elements)

    def test_find_with_sloppy_criteria(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'a', 'span', 'a')
        when(browser).find_elements_by_id("test1").thenReturn(elements)

        result = finder.find(browser, "id= test1  ")
        self.assertEqual(result, elements)

    def test_find_by_id_with_synonym_and_constraints(self):
        finder = ElementFinder()
        browser = mock()

        elements = self._make_mock_elements('div', 'input', 'span', 'input', 'a', 'input', 'div', 'input')
        elements[1].set_attribute('type', 'radio')
        elements[3].set_attribute('type', 'checkbox')
        elements[5].set_attribute('type', 'text')
        elements[7].set_attribute('type', 'file')
        when(browser).find_elements_by_id("test1").thenReturn(elements)

        result = finder.find(browser, "id=test1")
        self.assertEqual(result, elements)
        result = finder.find(browser, "id=test1", tag='input')
        self.assertEqual(result, [elements[1], elements[3], elements[5], elements[7]])
        result = finder.find(browser, "id=test1", tag='radio button')
        self.assertEqual(result, [elements[1]])
        result = finder.find(browser, "id=test1", tag='checkbox')
        self.assertEqual(result, [elements[3]])
        result = finder.find(browser, "id=test1", tag='text field')
        self.assertEqual(result, [elements[5]])
        result = finder.find(browser, "id=test1", tag='file upload')
        self.assertEqual(result, [elements[7]])

    def _make_mock_elements(self, *tags):
        elements = []
        for tag in tags:
            element = self._make_mock_element(tag)
            elements.append(element)
        return elements

    def _make_mock_element(self, tag):
        element = mock()
        element.tag_name = tag
        element.attributes = {}

        def set_attribute(name, value):
            element.attributes[name] = value
        element.set_attribute = set_attribute

        def get_attribute(name):
            return element.attributes[name]
        element.get_attribute = get_attribute

        return element
