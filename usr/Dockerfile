FROM ruby:3.3
WORKDIR /usr/src/app

# Dependency installation and cache layer creation
COPY Gemfile Gemfile.lock ./
RUN bundle install

# https://github.com/lycheeverse/lychee
# Checks for broken links
ADD https://github.com/lycheeverse/lychee/releases/download/lychee-v0.18.0/lychee-x86_64-unknown-linux-gnu.tar.gz /tmp
RUN tar -xvf /tmp/lychee-x86_64-unknown-linux-gnu.tar.gz -C /usr/local/bin \
    && chmod +x /usr/local/bin/lychee \
    && lychee --version


# Copy the rest of the application code
COPY . .
EXPOSE 4000
CMD ["jekyll", "serve", "--host", "0.0.0.0"]
