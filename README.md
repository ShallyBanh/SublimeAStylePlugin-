# SublimeAStylePlugin-

What is Astyle? Well Astyle stands for Artistic Style and is a source code indenter/formatter. In this plugin, the Astyle will be designed specifically for c/c++. 

# Inspiration
Why do this? Well it's extremely annoying when i try to format my code and I thought hey wouldn't it be nice if i just save my code and it automatically formatted itself so that's where the inspiration comes from. Also, because i'm hella lazy and i hate going through my code formatting it properly. 

Oh and another inspiration is that i have this really annoying friend who keeps starring my repos and pestering me to do things. So i figured i should do some stuff so maybe he'll leave me alone and stop starring my repos.

# Implementation
NOT COMPLETE YET. Currently all this does is fix the indentation and spacing of your code but there are some edge cases that will break it so i don't suggest using it until it's complete.

# Example Usage
Before
```c++
int main()
{
int i =1;
if (1==2)
{
int j =1;
}
}
```
After 
```c++
int main( )
{
  int i = 1;
  if ( 1 == 2 )
  {
    int j = 1;
  }
}
```

# TODO
A WHOLE LOT 
- <strike> Add fix to indentation to handle edge cases </strike>
- Test edge cases for indentation ^ (make sure that the fix actually works)
- Indentation for classes. Currently if you have classes in your file this won't work
- Test edge cases check for that ^
- <strike> Spacing for expressions, brackets, etc (ex. int i=1; -> int i = 1;) -> done </strike>
- Test edge cases for spacings ^
- Astyle options file where the user can specify the indentation level, spacing level, default brace level, etc they prefer
- Write test cases that i can run pre-commit to see if it'll break anything 
- Definitely forgetting something 

