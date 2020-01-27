# lexis-nexis-uni-downloader

This repository will help you download data from Nexis Uni. It is dockerized so it should work in most environments. It uses cookies directly from Google Chrome to authenticate with Nexis.

## Quickstart

1. Log into your univerity's Lexis Uni using **Google Chrome**.

2. Set the `LN_URL` environment variable.

    <details>
    <summary>Here are some examples:</summary>

    - Columbia: `export LN_URL=https://advance-lexis-com.ezproxy.cul.columbia.edu`
    - Harvard: `export LN_URL=https://advance-lexis-com.ezp-prod1.hul.harvard.edu`
    - Notre Dame: `export LN_URL=https://advance-lexis-com.proxy.library.nd.edu`
    - Multimedia University `export LN_URL=https://advance.lexis.com.proxyvlib.mmu.edu.my`
    - Boston University: `export LN_URL=http://www.lexisnexis.com.ezproxy.bu.edu`
    - Brenau University: `export LN_URL=https://advance-lexis-com.ezproxy.brenau.edu:2040`
    - Queens College: `export LN_URL=http://www.lexisnexis.com.queens.ezproxy.cuny.edu:2048`
    </details>

3. Run the setup:

    ```
    brew install AlJohri/-/kar
    kar setup
    ```

4. Get the authenticated cookies and export as environment variables.

    ```
    $(kar get-cookies)
    ```

    <details>
    <summary>Running into issues?</summary>

    This is the only part of the project that is not dockerized. If you run into issues with grabbing the cookies, manually get the cookies from Google Chrome. You can see which cookies are required in `scripts/get-cookies.py`. Export these three environment variables: `EZPROXY`, `MACHINE_ID`, and `SESSION_ID` before proceeding to the next step.
    </details>


5. Update `data/query.txt` as needed and download data.

    ```
    kar run python scripts/download-index.py
    kar run python scripts/download-documents.py
    ```

#### Simplify Development with Direnv

You can use [`direnv`](https://direnv.net/) to simplify development. This will automatically source the relevant environment variables when you `cd` into the project directory.

1. Install direnv: `brew install direnv`
2. Add the `direnv` hook into your shell profile: https://direnv.net/docs/hook.html
3. Add `export LN_URL=...` into a `.envrc` file.
4. Add the cookie environment variables into the `.envrc` file: `kar get-cookies >> .envrc`
5. Run `direnv allow` to mark the contents of the `.envrc` file as save for execution.

## Disclaimer

This library is not associated with Lexis Nexis. Please read the Lexis Nexis [terms of use](https://www.lexisnexis.com/terms/). Note that it is against the terms to use automatic software to download content. Use this software at your own risk.
