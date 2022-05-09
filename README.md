# mavr-sima

## Program

```python
class Program(Base):
    __tablename__ = 'programs'

    ID = Column(INTEGER, primary_key=True, index=True, unique=True)

    name = Column(VARCHAR(128), nullable=False, index=True)
    author = Column(VARCHAR(64), nullable=False, index=True)
    describe = Column(TEXT, nullable=True)
    
    marker = Column(VARCHAR(8))
    size1 = Column(NUMERIC(3, 1), default=9)
    size2 = Column(NUMERIC(3, 1), default=7)
    size3 = Column(NUMERIC(3, 1), default=5)
    period = Column(NUMERIC(3, 1), default=12)
```


## ObjectType

1. From Simbad
2. From Vizier
3. From Horizons
4. Custom object

## Object

```python
class ObservationObject(Base):  
    __tablename__ = 'objects'

    ID = Column(INTEGER, primary_key=True, index=True, unique=True)

    _Program = Column(INTEGER, ForeignKey('programs.ID'), default=1, index=True)

    type = Column(VARCHAR(1), index=True)

    main_id = Column(VARCHAR(32), nullable=False, index=True)
    name_list = Column(ARRAY(VARCHAR(32)), nullable=False)

    ra_2000 = Column(VARCHAR(16))
    dec_2000 = Column(VARCHAR(16))
    ra_2000_f = Column(NUMERIC(9, 6), nullable=True, index=True)
    dec_2000_f = Column(NUMERIC(10, 6), nullable=True, index=True)
    ra_pm = Column(NUMERIC(8, 3), nullable=True, default=None)
    dec_pm = Column(NUMERIC(8, 3), nullable=True, default=None)

    gmag = Column(NUMERIC(4, 2), nullable=True, default=None)
    bmag = Column(NUMERIC(4, 2), nullable=True, default=None)
    vmag = Column(NUMERIC(4, 2), nullable=True, default=None)
    rmag = Column(NUMERIC(4, 2), nullable=True, default=None)
    imag = Column(NUMERIC(4, 2), nullable=True, default=None)
    jmag = Column(NUMERIC(4, 2), nullable=True, default=None)
    hmag = Column(NUMERIC(4, 2), nullable=True, default=None)
    kmag = Column(NUMERIC(4, 2), nullable=True, default=None)

    sptype = Column(VARCHAR(32), nullable=True, default=None)
    parallax = Column(NUMERIC(7, 4), nullable=True, default=None)
    period = Column(NUMERIC(7, 4), nullable=True, default=None)

    status = Column(BOOLEAN, index=True)

    describe = Column(TEXT, nullable=True)

    posN = Column(SMALLINT, default=0)
    orbN = Column(SMALLINT, default=0)
```


## Position Parameter

```python
class PositionParameter(Base):
    __tablename__ = 'position_parameters'
    ID = Column(INTEGER, primary_key=True, index=True, unique=True)

    _Object = Column(INTEGER, ForeignKey('objects.ID'), nullable=False)

    type = Column(VARCHAR(16), nullable=False, default='Prepublished', index=True)

    epoch = Column(NUMERIC(10, 6), nullable=False)
    rho   = Column(NUMERIC(8, 4), nullable=False)
    rho_err = Column(NUMERIC(6, 4), nullable=True)
    theta = Column(NUMERIC(7, 4), nullable=False)
    theta_err = Column(NUMERIC(6, 4), nullable=True)
    theta_ambiguity = Column(BOOLEAN, default=False)
    dm = Column(NUMERIC(5, 3), nullable=True)
    dm_err = Column(NUMERIC(4, 3), nullable=True)
    filter = Column(VARCHAR(16))

    first_author = Column(VARCHAR(16), nullable=False, index=True)
    author = Column(TEXT, nullable=True)
    title = Column(VARCHAR(256), nullable=True)
    year = Column(SMALLINT, nullable=True)
    journal = Column(VARCHAR(256), nullable=True)
    doi = Column(VARCHAR(128), nullable=True)
    comment = Column(TEXT, nullable=True)
```

## Orbit

```python
class Orbit(Base):
    __tablename__ = 'orbits'

    ID = Column(INTEGER, primary_key=True, index=True, unique=True)
    
    _Object = Column(INTEGER, ForeignKey('objects.ID'), nullable=False)

    type = Column(VARCHAR(16), nullable=False, default='Prepublished')

    P = Column(NUMERIC(7, 4), nullable=False)
    T0 = Column(NUMERIC(8, 4), nullable=False)
    a = Column(NUMERIC(8, 4), nullable=False)
    e = Column(NUMERIC(5, 4), nullable=False)
    W = Column(NUMERIC(7, 4), nullable=False)
    w = Column(NUMERIC(7, 4), nullable=False)
    i = Column(NUMERIC(7, 4), nullable=False)

    P_err = Column(NUMERIC(6, 4), nullable=True)
    T0_err = Column(NUMERIC(6, 4), nullable=True)
    a_err = Column(NUMERIC(6, 4), nullable=True)
    e_err = Column(NUMERIC(6, 4), nullable=True)
    W_err = Column(NUMERIC(6, 4), nullable=True)
    w_err = Column(NUMERIC(6, 4), nullable=True)
    i_err = Column(NUMERIC(6, 4), nullable=True)

    first_author = Column(VARCHAR(16))
    author = Column(TEXT)
    title = Column(VARCHAR(256))
    year = Column(SMALLINT)
    journal = Column(VARCHAR(256))
    doi = Column(VARCHAR(128))
    comment = Column(TEXT)
```

## Journal

```python
class Journal(Base):
    __tablename__ = 'journal'

    ID = Column(INTEGER, primary_key=True, index=True, unique=True)
    
    _Object = Column(INTEGER, ForeignKey('objects.ID'))
    
    ra_start = Column(VARCHAR(16))
    dec_start = Column(VARCHAR(16))
    utc_date_start = Column(DateTime)
    lst_date_start = Column(TIME)
    z_start = Column(NUMERIC(4, 2))
    par_ang_start = Column(NUMERIC(5, 2))

    ra_end = Column(VARCHAR(16))
    dec_end = Column(VARCHAR(16))
    utc_date_end = Column(DateTime)
    lst_date_end = Column(TIME)    
    z_end = Column(NUMERIC(4, 2))
    par_ang_end = Column(NUMERIC(5, 2))

    filt = Column(VARCHAR(16))
    gain = Column(SMALLINT)
    mag = Column(SMALLINT)

    focus = Column(NUMERIC(5, 2))

    par_ang_mean = Column(NUMERIC(5, 2))

    t_in = Column(NUMERIC(4, 1))
    t_out = Column(NUMERIC(4, 1))
    t_mir = Column(NUMERIC(4, 1))
    press = Column(NUMERIC(4, 1))
    wind = Column(NUMERIC(4, 2))

    comment = Column(TEXT)
    lines = Column(TEXT)
```

## JournalNameEqual

```python
class JournalNameEqual(Base):
    __tablename__ = 'journal_name_equal'

    ID = Column(INTEGER, primary_key=True, index=True, unique=True)

    _Object = Column(INTEGER, ForeignKey('objects.ID'))
    
    journal_line = Column(TEXT)
    params = Column(JSON)
```
