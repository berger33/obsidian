---
id: software.seguranca.tranche16.001554
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/jpillora/chisel/master/README.md", "https://raw.githubusercontent.com/jpillora/chisel/master/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Camuflagem HTTP (**`--backend` Reverse Proxy**), TLS Nativo (**`--tls-domain` Let's Encrypt / `--tls-cert`**) e Customização de **`--header` / `Host`** no Chisel

## Em uma frase
Se um analista de segurança ou scanner externo acessar `https://seu-servidor:443` no navegador, como fazer o `chisel server` exibir uma página web legítima completa (como um site institucional ou servidor Nginx local) para qualquer visitante comum, **enquanto aceita silenciosamente conexões de túnel WebSocket apenas dos clientes Chisel autenticados na mesma porta `443`**?

## Por que importa
Usando a flag oficial **`--backend`** (ou seu alias `--proxy` em `main.go`)!

## Como funciona
Quando você inicia **`chisel server --port 443 --tls-domain tunel.exemplo.br --backend http://127.0.0.1:3000`**, o Chisel utiliza o `httputil.NewSingleHostReverseProxy` da biblioteca padrão do Go: qualquer requisição HTTP comum de navegador ou scanner que chegar na porta `443` é encaminhada de forma transparente para `http://127.0.0.1:3000` (ou qualquer site externo), e apenas requisições com o cabeçalho de handshake WebSocket do Chisel são direcionadas para o motor SSH interno!

## Exemplo
```bash
# Iniciar o chisel server com certificado TLS e reverse proxy de camuflagem (--backend) e conectar o cliente customizando cabecalhos HTTP (--header)
chisel server --port 8443 --keyfile ./server.key --tls-cert ./fullchain.pem --tls-key ./privkey.pem --backend https://example.com &
chisel client --fingerprint "${SERVER_FP}" \
  --header "User-Agent: Mozilla/5.0 (X11; Linux x86_64)" \
  --hostname "app.exemplo.br" \
  https://192.0.2.10:8443 R:127.0.0.1:1080:socks
```

## Limites e trade-offs
Veja no comando do `chisel client` acima as flags **`--header "HeaderName: HeaderContent"`** (validada pela função `setHeader` em `main.go`) e **`--hostname`**: elas permitem definir qualquer cabeçalho HTTP customizado (como `User-Agent`, tokens de autenticação de API Gateway/Cloudflare Access ou cabeçalhos de roteamento de Ingress) e sobrescrever o cabeçalho `Host` da requisição HTTP/WebSocket!

## Como verificar
Quando você usa `--tls-key` e `--tls-cert` no `chisel server`, o Chisel também monitora os arquivos de certificado em disco e os **recarrega automaticamente sem derrubar o servidor** sempre que o Certbot renova o certificado!

## Conexões
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Veja também: Sintaxe Completa de `<remote>` no Chisel: Tunelamento **Local (Forward)**, **Reverso (`R:`)**, **Proxy Dinâmico `SOCKS5` (`--socks5` / `R:socks`)** e **Túneis `UDP` (`/udp`)**.
- [[chisel-atravessando-proxies-corporativos-socks-http-connect-stdio-ssh]] — Veja também: Atravessando Proxies de Saída Corporativos (**`--proxy` HTTP CONNECT / SOCKS5**) e **SSH sobre HTTP (`stdio:` + `ssh -o ProxyCommand`)** com o Chisel.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
