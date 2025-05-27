class BeerSong:
    @classmethod
    def _validate(cls, verse):
        if not isinstance(verse, int):
            raise TypeError('Enter a whole number')
        if verse not in range(100):
            raise ValueError('Number must be between 0-99')
        return verse
    
    @classmethod
    def verse(cls, verse):
        verse = cls._validate(verse)
        
        if verse == 0:
            return (
                "No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
                )
        elif verse == 1:
            return (
                "1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall.\n"
                )
        elif verse == 2:
            return (
                f"{verse} bottles of beer on the wall, {verse} bottles of beer.\n"
                "Take one down and pass it around, 1 bottle of beer on the wall.\n"
                )
        else:
            return (
                f"{verse} bottles of beer on the wall, {verse} bottles of beer.\n"
                f"Take one down and pass it around, {verse - 1} bottles of beer on the wall.\n"
                )
    
    @classmethod
    def verses(cls, start, end):
        start = cls._validate(start)
        end = cls._validate(end)
        
        if end >= start:
            raise ValueError('End verse must be smaller than beginning verse')
        
        results = []
        for verse in range(start, end - 1, -1):
            results.append(BeerSong.verse(verse))
        
        return '\n'.join(results)
    
    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)

# print(BeerSong.lyrics())
# print('--------')
# print(BeerSong.verses(12, 10))
# print('--------')
# print(BeerSong.verse(1))
# print('--------')
# print(BeerSong.verses(4, 0))