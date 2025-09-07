from django import forms


class LoginForm(forms.Form):
    # দিলে → আপনি ফর্ম তৈরির সময় নিজের কাস্টম কাজ করতে পারবেন।
    # যেমনঃ প্রতিটি ফিল্ডে class="form-control" বসানো, placeholder দেওয়া, label বদলানো ইত্যাদি।
    # না দিলে → Django ডিফল্ট Form এর constructor চলবে। ফর্ম ঠিকই কাজ করবে, কিন্তু আপনার extra styling বা পরিবর্তন হবে না।
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #ei loop tar kaj holo form control newa. mane form er username password field er style er control newa. ei same kaj tai niche kora holo.
        # for field in self.fields:
        #     self.fields[field].widget.attrs.update({"class":"form-control"})
        
    username =forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        max_length=150,
        widget= forms.PasswordInput(attrs={"class":"form-control"})
    )
