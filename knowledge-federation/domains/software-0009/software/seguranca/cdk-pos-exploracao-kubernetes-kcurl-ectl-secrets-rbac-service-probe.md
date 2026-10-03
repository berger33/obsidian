---
id: software.seguranca.tranche10.000985
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/cdk-team/CDK/main/README.md", "https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CDK para **Kubernetes**: Clientes Nativos **`cdk kcurl`** (API Server), **`cdk ectl`** (`etcd`), Dump de `Secrets`/`ConfigMaps` e Descoberta de Componentes

## Em uma frase
Dentro de um Pod Kubernetes sem `kubectl` e sem `curl`, como um auditor testa se a `ServiceAccount` montada em `/var/run/secrets/kubernetes.io/serviceaccount/token` possui permissões RBAC excessivas para listar `Secrets`, `ConfigMaps` ou criar Pods privilegiados?

## Por que importa
O CDK traz embutido o utilitário **`cdk kcurl`**, que localiza automaticamente o token JWT da ServiceAccount padrão (ou usa um caminho de token informado), configura a CA do cluster e envia requisições `GET`/`POST` autenticadas para o **Kubernetes API Server**!

## Como funciona
Para auditoria automatizada de credenciais e configurações do cluster, o CDK inclui os módulos **`cdk run k8s-secret-dump`**, **`cdk run k8s-configmap-dump`**, **`cdk run k8s-psp-dump`**, **`cdk run k8s-get-sa-token`**, **`cdk run kubelet-exec`** e o cliente **`cdk ectl`** (para testar se o banco de dados **`etcd` na porta `2379`** está acessível sem autenticação mTLS)!

## Exemplo
```bash
# Consultar a API do Kubernetes a partir de um container distroless usando o cliente nativo cdk kcurl com o token da ServiceAccount atual
cdk kcurl default get "https://kubernetes.default.svc/api/v1/namespaces/default/pods" ""
```

## Limites e trade-offs
Como impedir que Pods que não precisam conversar com a API do Kubernetes tenham um token JWT montado no disco (`/var/run/secrets/kubernetes.io/serviceaccount/token`) esperando para ser lido por um atacante com `cdk kcurl`? Defina **`automountServiceAccountToken: false`** tanto na `ServiceAccount` `default` de cada namespace quanto no `spec` de todos os Pods de aplicação!

## Como verificar
Audite também se a porta `2379` do `etcd` e a porta `10250` do `kubelet` estão isoladas de Pods de aplicação através de **Kubernetes NetworkPolicies**.

## Conexões
- [[cdk-auditoria-docker-socket-api-runc-containerd-shim-ucurl-dcurl]] — Veja também: CDK: Comprometimento via **Docker Unix Socket (`docker.sock`, `ucurl`)**, **Docker TCP API (`:2375`, `dcurl`)**, `runc` (`CVE-2019-5736`) e `containerd-shim` (`CVE-2020-15257`).
- [[cdk-ferramentas-embutidas-net-tools-ps-netstat-ifconfig-probe-nc-vi]] — Veja também: CDK **Built-in Tool Module**: Como Operar em Containers Distroless usando **`cdk ps`**, **`cdk netstat`**, **`cdk ifconfig`**, **`cdk probe`**, **`cdk nc`** e **`cdk vi`**.
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
