---
id: software.devops.tranche11.001016
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://dexidp.io/docs/getting-started/", "https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Distribuição e implantação do Dex: imagens oficiais Alpine e Distroless, Helm chart e compilação com Go

## Em uma frase
O Dex é distribuído oficialmente como imagem de container em `ghcr.io/dexidp/dex` e `docker.io/dexidp/dex` em duas variantes (**`alpine`** e **`distroless`**), conta com um Helm chart oficial de referência em `charts.dexidp.io` e pode ser compilado a partir do código-fonte com `make build` em ambientes Go 1.19+.

## Por que importa
Em clusters Kubernetes de produção com políticas estritas de segurança de containers, escolher entre a variante `distroless` (sem shell nem gerenciador de pacotes para minimizar superfície de ataque) e a variante `alpine` (que inclui utilitários e pré-processamento no entrypoint) impacta diretamente como a configuração e o diagnóstico são operados.

## Como funciona
Segundo o guia oficial *Getting Started* (`dexidp.io/docs/getting-started/`), as imagens oficiais são publicadas no GitHub Container Registry (`ghcr.io/dexidp/dex`) e no Docker Hub (`docker.io/dexidp/dex`). Para implantações Kubernetes declarativas, o projeto mantém o chart Helm oficial em `https://charts.dexidp.io/`. Para desenvolvimento ou auditoria local do binário, basta clonar `https://github.com/dexidp/dex.git` em um ambiente com Go 1.19 ou superior e executar `make build` (que gera `./bin/dex`) e `make examples` (que compila `./bin/example-app`).

## Exemplo
```bash
# Instalar o Dex no Kubernetes usando o repositório oficial de Helm charts (charts.dexidp.io)
helm repo add dex https://charts.dexidp.io
helm repo update
helm upgrade --install dex dex/dex \
  --namespace auth \
  --create-namespace \
  -f values-dex.yaml
```

## Limites e trade-offs
Ao utilizar a variante de imagem `distroless`, não há shell (`/bin/sh`) dentro do container para depuração interativa com `kubectl exec`; caso precise diagnosticar conectividade de rede ou certificados LDAP de dentro do pod em produção, utilize containers efêmeros (`kubectl debug`) ou teste temporariamente com a variante `alpine`.

## Como verificar
Verifique a assinatura e a imagem em execução no cluster com `kubectl -n auth get pods -o jsonpath='{.items[*].spec.containers[*].image}'` e valide o endpoint `/healthz` do Dex.

## Conexões
- [[dex-limitacoes-protocolo-saml-aviso-seguranca-refresh-tokens]] — Veja também: Limitações de protocolo e alerta de segurança do conector SAML 2.0 no Dex.
- [[dex-configuracao-gomplate-expansao-variaveis-ambiente]] — Veja também: Configuração do Dex: pré-processamento com gomplate no entrypoint do container e expansão nativa de variáveis ($VAR / DEX_EXPAND_ENV).
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://dexidp.io/docs/getting-started/) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
