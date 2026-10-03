---
id: software.seguranca.tranche03.000241
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

# Pomerium: arquitetura do *Identity-Aware Access Proxy* baseado nos princípios Google BeyondCorp e NIST Zero Trust

## Em uma frase
Conforme documentado na página oficial *What is Pomerium?* (`pomerium.com/docs`) e no README do repositório (`pomerium/pomerium`, escrito em Go sob licença Apache 2.0), o **Pomerium** é um proxy reverso sensível à identidade e ao contexto (*Identity and Context-Aware Access Proxy*), construído sobre o motor de proxy **Envoy** e os princípios do **Google BeyondCorp** e **NIST Zero Trust Architecture (SP 800-207)**.

## Por que importa
VPNs corporativas tradicionais concedem acesso no nível da rede (Camada 3): uma vez conectado à VPN, o dispositivo do usuário enxerga toda a sub-rede interna e as aplicações internas muitas vezes confiam implicitamente em qualquer pacote que venha da rede interna.

## Como funciona
O Pomerium substitui a confiança baseada em localização de rede por **acesso sem cliente (*clientless access*) com verificação contínua por requisição**: cada requisição HTTP/gRPC/TCP para um serviço interno passa por três etapas obrigatórias — **1. Authenticate** (via seu IdP OIDC: Okta, Entra ID, Google, GitHub, Auth0, Keycloak), **2. Authorize** (avaliação de políticas de identidade, grupos, claims e estado do dispositivo no *Policy Engine*) e **3. Proxy** (encaminhamento seguro com injeção de identidade criptográfica)!

## Exemplo
```yaml
# Exemplo de configuração de rota protegida no config.yaml do Pomerium Core:
authenticate_service_url: https://authenticate.internal.corp
idp_provider: oidc
idp_provider_url: https://dex.internal.corp/dex
idp_client_id: pomerium-proxy

routes:
  - from: https://grafana.internal.corp
    to: http://grafana.monitoring.svc.cluster.local:3000
    policy:
      - allow:
          and:
            - domain:
                is: internal.corp
```

## Limites e trade-offs
Como detalha a documentação oficial (`pomerium.com/docs`), o **Pomerium Core** é o servidor open-source e motor de data-plane auto-gerenciado, podendo operar em modo *All-in-One* ou distribuído em componentes independentes (`Authenticate`, `Authorize`, `Proxy` e `Databroker`).

## Como verificar
Execute `pomerium --version` e acesse uma rota protegida verificando o redirecionamento automático para o IdP.

## Conexões
- [[pomerium-policy-language-ppl-operadores-allow-deny-and-or-not-nor]] — Veja também: Pomerium Policy Language (`PPL`): autorização declarativa com operadores lógicos (`allow`/`deny`, `and`, `or`, `not`, `nor`) e critérios de contexto.

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
