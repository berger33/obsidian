---
id: software.seguranca.tranche03.000247
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

# Pomerium Arquitetura de Serviços Distribuídos (`Authenticate`, `Authorize`, `Proxy` e `Databroker`): isolamento e escalabilidade

## Em uma frase
Para implantações de produção de alta escala, o Pomerium Core pode ser desmembrado (via variável `SERVICES=` ou Helm chart) em quatro serviços independentes comunicando-se via gRPC autenticado por `shared_secret`: **`proxy`** (data-plane Envoy na borda), **`authenticate`** (fluxos OAuth2/OIDC com o IdP), **`authorize`** (motor de avaliação de políticas PPL e OPA) e **`databroker`** (armazenamento de estado de sessões, rotas e diretórios).

## Por que importa
Escalar todo o monolito quando apenas o tráfego de data-plane (`proxy`) aumentou 10x desperdiça recursos, além de expor as credenciais OAuth2 do IdP (`idp_client_secret`) nos pods de borda.

## Como funciona
Na topologia distribuída: 1) apenas os pods **`proxy`** e **`authenticate`** recebem tráfego externo; 2) apenas o **`authenticate`** precisa das credenciais do IdP; 3) o **`authorize`** avalia políticas em memória com baixa latência; e 4) o **`databroker`** persiste o estado em backend durável!

## Exemplo
```bash
# Exemplo de variáveis de ambiente para iniciar uma réplica dedicada apenas ao data-plane (Proxy) do Pomerium:
export SERVICES="proxy"
export AUTHORIZE_SERVICE_URL="https://authorize.pomerium.svc.cluster.local:5443"
export DATABROKER_SERVICE_URL="https://databroker.pomerium.svc.cluster.local:5443"
export SHARED_SECRET="base64-encoded-32-byte-secret..."
pomerium -config /etc/pomerium/config.yaml
```

## Limites e trade-offs
Gere o `shared_secret` e o `cookie_secret` com exatamente **32 bytes aleatórios codificados em Base64** (`head -c32 /dev/urandom | base64`) e rotacione-os periodicamente.

## Como verificar
Verifique a saúde individual de cada serviço nos endpoints `/ping` e `/healthz` do Pomerium.

## Conexões
- [[pomerium-kubernetes-ingress-controller-gateway-api-crd-annotations]] — Veja também: Pomerium Kubernetes Ingress Controller e Gateway API: definição declarativa de rotas e políticas via `Ingress` Annotations e CRDs.
- [[pomerium-integracao-kubernetes-dashboard-api-impersonation-serviceaccount]] — Veja também: Pomerium para Acesso Zero-Trust a `Kubernetes API` e Dashboards Internos: injeção de credenciais upstream e cabeçalhos `Impersonate-*`.

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
