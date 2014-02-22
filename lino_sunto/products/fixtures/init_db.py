from lino.utils.instantiator import Instantiator, i2d


def objects():
    def specopts(prod, specdict, optdict):

        spec = Instantiator(
            'products.ProductSpec',
            "specification specification_value",
            product=prod
        )

        option = Instantiator(
            'products.ProductOption',
            "option option_value",
            product=prod
        )

        for key, value in specdict:
            yield spec.build(key, value)

        for key, value in optdict:
            yield option.build(key, value)

    manufacturer = Instantiator('products.Manufacturer', 'name')
    manuflist = ["Apple", "Adobe", "Microsoft", "snom", "Cisco", "HP", "QNAP", "LaCie", "Samsung"]

    for manuf in manuflist:
        yield manufacturer.build(manuf)

    product = Instantiator(
        'products.Product',
        "manufacturer:name name model_number line production_begin supported"
    ).build

    prods = product("Apple", "MacBook Air", "A1466", "13\" Mid 2013", i2d(20101001), True)
    specs = [
        ["CPU", "1.3GHz dual-core Intel Core i5 (Turbo Boost up to 2.6GHz) with 3MB shared L3 cache"],
        ["Memory", "4GB of 1600MHz LPDDR3 onboard memory"],
        ["Graphics", "Intel HD Graphics 5000"],
        ["Camera", "720p FaceTime HD camera"],
        ["USB Connections", "2x USB 3 ports (up to 5 Gbps)"],
        ["Thunderbolt Connections", "Thunderbolt port"],
        ["Power Connections", "MagSafe 2 power port"],
        ["Other Connections", "SDXC card slot"],
        ["Wireless", "802.11ac Wi-Fi networking;3 IEEE 802.11a/b/g/n compatible"],
        ["Bluetooth", "Bluetooth 4.0 wireless technology"],
        ["Audio Speaker", "Stereo speakers"],
        ["Audio Microphone", "Dual microphones"],
        ["Audio Headphone", "Headphone port"],
        ["Keyboard", ("Full-size backlit keyboard with 78 or 79 (ISO) keys, including 12 function keys and"
                      "4 arrow keys (inverted T arrangement) with ambient light sensor")],
        ["Trackpad", ("Multi-Touch trackpad for precise cursor control; supports inertial scrolling, pinch,"
                      "rotate swipe, three-finger swipe, four-finger swipe, tap, double-tap, and drag capabilities")],
        ["Battery", "Built-in 54-watt-hour lithium-polymer battery"],
        ["Power", "45W MagSafe 2 Power Adapter with cable management; MagSafe 2 power port"],
        ["OS", "OS X Mountain Lion"],
        ["Software", "iLife"]
    ]
    opts = [
        ["CPU", "1.7GHz dual-core Intel Core i7 (Turbo Boost up to 3.3GHz) with 4MB shared L3 cache"],
        ["HDD 1", "256GB SSD"],
        ["HDD 2", "512GB SSD"],
        ["Memory", "8GB of 1600MHz LPDDR3 onboard memory"]
    ]
    yield prods
    yield specopts(prods, specs, opts)

    example = [
        ["one", "1"],
        ["two", "2"],
        ["three", "3"]
    ]

    prods = product("Apple", "MacBook Air", "A1465", "11\" Mid 2013", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1466", "13\" Mid 2012", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1465", "11\" Mid 2012", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1369", "13\" Mid 2011", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1370", "11\" Mid 2011", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1369", "13\" Mid 2010", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1370", "11\" Mid 2010", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1304", "Mid 2009", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1304", "Late 2008", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)

    prods = product("Apple", "MacBook Air", "A1237", "Initial Release", i2d(20101001), True)
    specs = example
    opts = example
    yield prods
    yield specopts(prods, specs, opts)