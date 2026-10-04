---
id: software.seguranca.tranche10.000987
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

# CDK: Auditoria de **Cloud Metadata API (IMDS)**, Varredura de Chaves (**`ak-leakage`**), Sidecar **Istio (`istio-check`)** e `route_localnet` (`CVE-2020-8558`)

## Em uma frase
Além de contêineres e Kubernetes puros, o CDK audita a fronteira entre o Pod, a malha de serviço (*Service Mesh*) e a nuvem subjacente (AWS, Alibaba Cloud, Tencent Cloud, GCP, Azure).

## Por que importa
Durante o `cdk eva --full` e nos módulos dedicados, quatro verificações se destacam: **(1) Cloud Provider Metadata API** — testa se o container consegue alcançar o IP de link-local **`169.254.169.254`** (IMDSv1) para extrair credenciais IAM da instância do nó; **(2) `cdk run ak-leakage <diretorio>`** — varre arquivos de configuração e código dentro do container em busca de Access Keys e segredos; **(3) `cdk run istio-check`** — inspeciona metadados e configurações do proxy Envoy quando o Pod faz parte de uma malha **Istio**; e **(4) `CVE-2020-8558` (`net.ipv4.conf.all.route_localnet`)** — verifica se o `kube-proxy` deixou `route_localnet=1`, o que permitia a nós adjacentes alcançar serviços escutando em `127.0.0.1` do host!

## Como funciona
Bloquear o acesso de Pods de aplicação ao IP `169.254.169.254` e exigir **IMDSv2 (`HttpTokens: required` com `HttpPutResponseHopLimit: 1`)** nos nós EC2 neutraliza o roubo de credenciais de instância via IMDSv1!

## Exemplo
```bash
# Executar o scanner interno de chaves e segredos do CDK (ak-leakage) sobre o diretorio da aplicacao no container
cdk run ak-leakage /app
```

## Limites e trade-offs
Por que configurar **`HttpPutResponseHopLimit = 1`** junto com **`HttpTokens = required` (IMDSv2)** nas instâncias EC2 que servem como nós Kubernetes é uma defesa tão eficaz? Porque todo pacote enviado de dentro de um Pod em rede bridge/overlay passa por um salto de roteamento (*hop*) ao sair do namespace do container, fazendo o TTL do `PUT` do IMDSv2 chegar em `0` e ser descartado antes de atingir o serviço de metadados da instância!

## Como verificar
Audite essa configuração em todas as suas instâncias EC2 usando o **Steampipe (`aws_ec2_instance.metadata_options`)** ou o **KICS**.

## Conexões
- [[cdk-ferramentas-embutidas-net-tools-ps-netstat-ifconfig-probe-nc-vi]] — Veja também: CDK **Built-in Tool Module**: Como Operar em Containers Distroless usando **`cdk ps`**, **`cdk netstat`**, **`cdk ifconfig`**, **`cdk probe`**, **`cdk nc`** e **`cdk vi`**.
- [[cdk-auditoria-persistencia-kubernetes-daemonset-cronjob-shadow-apiserver]] — Veja também: Análise de Técnicas de **Persistência em Kubernetes** Mapeadas pelo CDK (`k8s-backdoor-daemonset`, `k8s-cronjob`, `k8s-shadow-apiserver` e `CVE-2020-8554`).
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.
- [[peirates-coleta-credenciais-cloud-imds-aws-gcp-kops-s3-gcs]] — Referência cruzada direta com peirates-coleta-credenciais-cloud-imds-aws-gcp-kops-s3-gcs.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
