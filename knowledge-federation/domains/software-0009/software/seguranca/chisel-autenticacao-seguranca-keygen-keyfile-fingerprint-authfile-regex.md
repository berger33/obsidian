---
id: software.seguranca.tranche16.001552
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

# Blindando o Chisel Contra MITM e Acesso Não Autorizado: **`--keygen` / `--keyfile`**, Pinning de **`--fingerprint`** e Controle de Acesso **`--authfile` (`users.json`)**

## Em uma frase
O que acontece se você subir um `chisel server` na nuvem sem configurar `--auth` / `--authfile` e conectar o `chisel client` sem passar `--fingerprint`? **(1)** Qualquer pessoa na internet que descobrir a porta do seu servidor poderá abrir túneis nele, e **(2)** Um atacante no caminho da rede poderia interceptar a conexão inicial (*Man-in-the-Middle*) porque o servidor gera uma chave efêmera nova a cada reinicialização!

## Por que importa
Como blindar 100% a autenticação mútua e a autorização de túneis no Chisel conforme documentado em `README.md` e `main.go`?

## Como funciona
Em três passos: **(1) Gere uma chave privada SSH ECDSA persistente no servidor** com **`chisel server --keygen /etc/chisel/server.key`** e inicie o servidor com **`--keyfile /etc/chisel/server.key`** (nota: a flag antiga `--key` foi depreciada!); **(2) Fixe a impressão digital da chave pública no cliente** passando **`chisel client --fingerprint <SHA256_FINGERPRINT>`**; e **(3) Restrinja quais usuários podem abrir quais portas/IPs** usando **`--authfile /etc/chisel/users.json`**!

## Exemplo
```json
{
  "operador_alice:SenhaForteAqui123!": [
    "^127\\.0\\.0\\.1:5432$",
    "^R:127\\.0\\.0\\.1:8080$"
  ]
}
```

## Limites e trade-offs
Preste muita atenção ao alerta de segurança documentado na seção `--authfile` do `README.md` oficial sobre as expressões regulares do `users.json` acima: **Os padrões regex no `users.json` NÃO são ancorados por padrão!** Se você escrever `"10.0.0.1:80"` sem `^` e `$`, ele também permitirá `"210.0.0.1:8080"` (e o ponto `.` casa com qualquer caractere)! Portanto, **SEMPRE ancore suas expressões regulares no `users.json` com `^` no início, `\.` escapado e `$` no final** (ex.: `"^10\\.0\\.0\\.1:80$"`)!

## Como verificar
Outro detalhe importante do `--authfile` documentado no `README.md`: o arquivo `users.json` sofre **Hot-Reload automático** sempre que é salvo em disco, e para permitir que um usuário use o proxy SOCKS5 você deve incluir explicitamente `"^socks$"` na lista de permissões dele!

## Conexões
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Veja também: Arquitetura do **Chisel (`jpillora/chisel`)**: Tunelamento Rápido **TCP e UDP** Encapsulado sobre **HTTP / WebSockets** e Criptografado via **SSH (`crypto/ssh`)**.
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Veja também: Sintaxe Completa de `<remote>` no Chisel: Tunelamento **Local (Forward)**, **Reverso (`R:`)**, **Proxy Dinâmico `SOCKS5` (`--socks5` / `R:socks`)** e **Túneis `UDP` (`/udp`)**.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
