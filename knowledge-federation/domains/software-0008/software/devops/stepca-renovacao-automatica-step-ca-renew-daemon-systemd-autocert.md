---
id: software.devops.tranche20.001936
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/smallstep/cli/master/README.md", "https://raw.githubusercontent.com/smallstep/certificates/master/README.md", "https://github.com/smallstep/certificates"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Smallstep Renovação Automática e Revogação Passiva: `step ca renew --daemon`, timers systemd e Kubernetes `autocert`

## Em uma frase
A filosofia de **revogação passiva** do `step-ca` baseia-se em emitir certificados com vida útil curta (como `24h`) e automatizar sua renovação contínua via **`step ca renew --daemon`** (quando o cliente já possui o certificado mTLS atual antes do vencimento), timers systemd ou o controlador Kubernetes **`autocert`** / **`step-issuer`**.

## Por que importa
Se um certificado dura apenas 24 horas e o mecanismo de renovação falhar em recarregar o processo do NGINX/Envoy/PostgreSQL após gravar o novo arquivo `.crt` em disco, o serviço sairá do ar no dia seguinte.

## Como funciona
O comando `step ca renew --daemon --exec "nginx -s reload" srv.crt srv.key` fica em execução em background, calcula automaticamente o momento de renovação (por padrão quando resta 1/3 da vida útil do certificado, ~16h de um certificado de 24h), renova via mTLS junto ao `step-ca` e executa o comando passado em `--exec` para recarregar o serviço sem downtime.

## Exemplo
```bash
# Iniciando o daemon de renovação contínua que recarrega o serviço a cada rotação:
step ca renew --daemon \
  --exec "systemctl reload nginx" \
  /etc/ssl/certs/service.crt /etc/ssl/private/service.key
```

## Limites e trade-offs
Para verificar em scripts de monitoramento se um certificado em disco ou em um endpoint HTTPS precisa ser renovado dentro de uma janela específica, utilize `step certificate needs-renewal --expires-in 8h service.crt` (que retorna código de saída `0` quando precisa renovar).

## Como verificar
Teste `step certificate needs-renewal` contra um certificado emitido e valide o código de retorno `$?`.

## Conexões
- [[stepca-step-certificate-create-inspect-lint-verify-rfc5280]] — Veja também: Smallstep `step certificate`: criação, inspeção, `lint` (RFC 5280 / CA-Browser Forum) e verificação de certificados X.509.
- [[stepca-step-crypto-jose-jwt-jwk-jws-jwe-totp-kdf]] — Veja também: Smallstep `step crypto` e `step oauth`: toolkit de linha de comando para JWT, JWK, JWS, JWE, NaCl, TOTP e fluxos OAuth/OIDC.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/certificates) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
