---
id: software.devops.tranche20.001935
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
fontes: ["https://raw.githubusercontent.com/smallstep/cli/master/README.md", "https://raw.githubusercontent.com/smallstep/certificates/master/README.md", "https://github.com/smallstep/cli"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Smallstep `step certificate`: criação, inspeção, `lint` (RFC 5280 / CA-Browser Forum) e verificação de certificados X.509

## Em uma frase
O grupo de comandos **`step certificate`** da CLI `step` permite criar pares de chaves (`RSA`, `ECDSA`, `EdDSA`), gerar CAs e certificados folha (`create`), assinar CSRs (`sign`), inspecionar certificados locais ou remotos (`inspect`), validar cadeias (`verify`) e executar **linting de conformidade (`step certificate lint`)** contra a RFC 5280 e o CA/Browser Forum.

## Por que importa
Um certificado TLS emitido com extensões X.509 incorretas (como falta de `SubjectAltName`, `KeyUsage` incompatível ou validade excessiva) pode funcionar no `curl -k` mas falhar silenciosamente em navegadores Chrome/Safari ou em clientes iOS/macOS.

## Como funciona
O comando `step certificate lint` analisa estaticamente o certificado em disco ou diretamente de uma URL HTTPS remota e aponta qualquer desvio das normas RFC 5280, enquanto `step certificate inspect --short` exibe um resumo limpo de SANs, validade e emissor.

## Exemplo
```bash
# Criando um certificado local com perfil leaf e validando sua conformidade RFC 5280:
step certificate create api.local api.crt api.key \
  --profile leaf --not-after=24h --no-password --insecure
step certificate inspect api.crt --short
step certificate lint api.crt
```

## Limites e trade-offs
Ao usar `step certificate inspect https://servico.corp.internal:8443 --roots root_ca.crt`, a CLI faz o handshake TLS real com o servidor remoto e inspeciona toda a cadeia apresentada em rede.

## Como verificar
Execute `step certificate lint <arquivo.crt>` em seus certificados para garantir zero erros de conformidade X.509.

## Conexões
- [[stepca-ssh-certificate-authority-single-sign-on-user-host-certs]] — Veja também: Smallstep `step-ca` SSH Certificate Authority: substituição de `authorized_keys` e `known_hosts` por certificados SSH via SSO.
- [[stepca-renovacao-automatica-step-ca-renew-daemon-systemd-autocert]] — Veja também: Smallstep Renovação Automática e Revogação Passiva: `step ca renew --daemon`, timers systemd e Kubernetes `autocert`.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/cli) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
