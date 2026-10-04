---
id: software.devops.tranche09.000888
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md", "https://telepresence.io/docs/concepts/architecture", "https://github.com/telepresenceio/telepresence"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Telepresence: instalação e administração do Traffic Manager no cluster (telepresence helm install/upgrade) e escopo de namespaces

## Em uma frase
O **Traffic Manager** é instalado no cluster pelo administrador via Helm chart oficial ou pelo comando embutido `telepresence helm install` (`upgrade` / `uninstall`), permitindo restringir quais namespaces são gerenciados e configurar permissões RBAC para os desenvolvedores.

## Por que importa
Em clusters corporativos multi-equipe, administradores de plataforma precisam controlar a versão do `Traffic Manager` via GitOps/Helm, limitar a atuação do Telepresence apenas aos namespaces de desenvolvimento autorizados e garantir que os desenvolvedores não precisem de permissões `cluster-admin` para realizar `connect` e `intercept`. A página `Architecture` (`telepresence.io/docs/concepts/architecture`) detalha o papel administrativo do `Traffic Manager`.

## Como funciona
Conforme documentado oficialmente, o `Traffic Manager` (instalado por padrão no namespace `ambassador`) pode ser implantado de duas formas equivalentes: (1) usando o Helm chart embutido diretamente no binário cliente via **`telepresence helm install`** (aceitando customizações com `--set` ou `-f values.yaml`, atualizado com `telepresence helm upgrade` e removido com `telepresence helm uninstall`); ou (2) usando o CLI do `helm` diretamente a partir do Artifact Hub (`telepresence-oss`). Uma vez que o administrador instalou o `Traffic Manager`, os desenvolvedores comuns precisam apenas de permissões RBAC em nível de namespace (`port-forward`/acesso ao serviço do `traffic-manager` e permissão nos seus próprios Deployments) para usar `telepresence connect` e `telepresence intercept`.

## Exemplo
```bash
# Instalar ou atualizar o Traffic Manager no cluster passando valores customizados de Helm e encerrar a sessão local
telepresence helm upgrade --namespace ambassador
telepresence quit -s
```

## Limites e trade-offs
Para evitar incompatibilidades de protocolo gRPC entre as estações de trabalho dos desenvolvedores e o cluster, mantenha a versão do binário cliente `telepresence` nas máquinas dos engenheiros alinhada à versão do `Traffic Manager` instalado no cluster (verificável com `telepresence version`, que exibe tanto a versão do `Client` quanto a do `Traffic Manager` conectado).

## Como verificar
Execute `telepresence version` enquanto conectado ao cluster para confirmar a compatibilidade de versões entre `Client`, `Root Daemon`, `User Daemon` e `Traffic Manager`.

## Conexões
- [[telepresence-execucao-containers-docker-run-docker-build]] — Veja também: Telepresence: execução de interceptações em containers Docker locais (--docker-run, --docker-build e telepresence connect --docker).
- [[telepresence-modos-nao-intrusivos-wiretap-ingest-producao-staging]] — Veja também: Telepresence: depuração não-intrusiva com wiretap (cópia de tráfego) e ingest (apenas variáveis/volumes).
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[telepresence-modos-traffic-agent-sidecar-vs-node-agent]] — Referência cruzada direta com telepresence-modos-traffic-agent-sidecar-vs-node-agent.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
