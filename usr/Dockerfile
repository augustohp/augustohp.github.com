FROM ruby:3.3
WORKDIR /usr/src/app

# Dependency installation and cache layer creation
COPY Gemfile Gemfile.lock ./
RUN bundle install

# https://github.com/lycheeverse/lychee
# Checks for broken links
ADD https://github.com/lycheeverse/lychee/releases/download/lychee-v0.24.2/lychee-x86_64-unknown-linux-musl.tar.gz /tmp
RUN tar -xvf /tmp/lychee-x86_64-unknown-linux-musl.tar.gz --strip-components=1 \
        -C /usr/local/bin lychee-x86_64-unknown-linux-musl/lychee \
    && chmod +x /usr/local/bin/lychee \
    && lychee --version


# Copy the rest of the application code
COPY . .
EXPOSE 4000
CMD ["jekyll", "serve", "--host", "0.0.0.0"]
