---
id: software.seguranca.tranche03.000245
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://www.pomerium.com/docs", "https://raw.githubusercontent.com/pomerium/pomerium/main/README.md", "https://github.com/pomerium/pomerium"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pomerium Rotas `TCP` (`tcp+https://`): acesso Zero-Trust a bancos de dados (`PostgreSQL`, `Redis`), `SSH` e `RDP` sem VPN

## Em uma frase
Além de aplicações web HTTP/HTTPS e gRPC, o Pomerium protege **qualquer serviço baseado em TCP puro** (como **SSH**, **PostgreSQL**, **MySQL**, **Redis**, **Kubernetes API** e **RDP**) encapsulando a conexão TCP sobre um túnel HTTPS autenticado e autorizado por identidade (**`from: tcp+https://host:porta`**)!

## Por que importa
Muitas empresas conseguem colocar suas aplicações web atrás de um proxy SSO, mas mantêm um servidor de VPN legado aberto apenas porque os engenheiros precisam conectar-se via SSH ou cliente SQL (`psql`) em bancos de dados internos.

## Como funciona
Com uma rota `from: tcp+https://postgres.internal.corp:5432` -> `to: tcp://10.0.20.15:5432`, o engenheiro usa a CLI **`pomerium-cli tcp`** (ou suporte nativo `ProxyCommand` no `~/.ssh/config`): a CLI abre o navegador para autenticar no IdP com MFA, estabelece um listener local em `127.0.0.1` e o Pomerium valida a política PPL antes de permitir o túnel TCP!

## Exemplo
```yaml
# Protegendo um servidor SSH e um banco PostgreSQL internos via túnel TCP+HTTPS do Pomerium:
routes:
  - from: tcp+https://ssh-bastion.internal.corp:22
    to: tcp://10.10.1.50:22
    policy:
      - allow:
          and:
            - claim/groups:
                has: infra-ssh-access
```

## Limites e trade-offs
Para conexões SSH, configure no `~/.ssh/config` do desenvolvedor a diretiva `ProxyCommand pomerium-cli tcp %h:%p`, tornando o comando `ssh usuario@ssh-bastion.internal.corp` 100% transparente!

## Como verificar
Teste iniciar o listener local com `pomerium-cli tcp ssh-bastion.internal.corp:22 --listen 127.0.0.1:2222`.

## Conexões
- [[pomerium-mtls-downstream-upstream-client-certificates-device-identity]] — Veja também: Pomerium `mTLS` Downstream (Certificados de Cliente/Dispositivo) e Upstream (Criptografia Mútua Proxy -> Backend).
- [[pomerium-kubernetes-ingress-controller-gateway-api-crd-annotations]] — Veja também: Pomerium Kubernetes Ingress Controller e Gateway API: definição declarativa de rotas e políticas via `Ingress` Annotations e CRDs.

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
