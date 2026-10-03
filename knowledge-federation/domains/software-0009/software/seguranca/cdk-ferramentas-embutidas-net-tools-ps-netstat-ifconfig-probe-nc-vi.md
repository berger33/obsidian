---
id: software.seguranca.tranche10.000986
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

# CDK **Built-in Tool Module**: Como Operar em Containers Distroless usando **`cdk ps`**, **`cdk netstat`**, **`cdk ifconfig`**, **`cdk probe`**, **`cdk nc`** e **`cdk vi`**

## Em uma frase
Containers de produção baseados em `gcr.io/distroless/static` ou imagens minimalistas frequentemente removem pacotes como `procps` (`ps`), `net-tools` (`ifconfig`, `netstat`), `iproute2` (`ip`, `ss`), `nmap`/`nc` e editores de texto (`vi`/`nano`).

## Por que importa
Para permitir diagnóstico completo de rede e processos sem instalar pacotes nem tocar em repositórios apt/apk (o que geraria alertas imediatos e falharia em rootfs `readOnlyRootFilesystem: true`), o **Módulo Tool do CDK** reimplementa esses utilitários diretamente no binário Go (usando `gopsutil`, `tcell` e `golang.org/x/sys`)!

## Como funciona
Basta executar: **`cdk ps`** (lista processos lendo `/proc` como `ps -ef`), **`cdk netstat`** (lista conexões e portas abertas como `netstat -antup`), **`cdk ifconfig`** (interfaces e IPs), **`cdk vi <arquivo>`** (editor visual de terminal!), **`cdk nc`** (túnel TCP) e **`cdk probe <faixa_ip> <portas> <paralelismo> <timeout_ms>`** (scanner TCP rápido de rede interna)!

## Exemplo
```bash
# Inspecionar processos, conexoes de rede ativas, interfaces e sondar portas internas usando os utilitarios embutidos do CDK
cdk ps
cdk netstat
cdk ifconfig
cdk probe 10.96.0.1-20 80,443,2379,6443,8080,10250 50 800
```

## Limites e trade-offs
Para equipes de **Defesa em Runtime (KubeArmor / Tracee)**: muitos engenheiros acreditam que remover `/bin/ps`, `/bin/netstat` e `/usr/bin/curl` da imagem Docker impede o reconhecimento caso o atacante suba um binário estático; o Módulo Tool do CDK prova por que a remoção de binários na imagem precisa ser combinada com **`readOnlyRootFilesystem: true` + `noexec` em `/tmp` e `/dev/shm` + bloqueio de execução de binários não-autorizados via KubeArmor/AppArmor**!

## Como verificar
Verifique em seus clusters se os diretórios graváveis de containers (`/tmp`, `/var/tmp`, `/dev/shm`) impedem a gravação e execução de binários externos.

## Conexões
- [[cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe]] — Veja também: CDK para **Kubernetes**: Clientes Nativos **`cdk kcurl`** (API Server), **`cdk ectl`** (`etcd`), Dump de `Secrets`/`ConfigMaps` e Descoberta de Componentes.
- [[cdk-auditoria-cloud-metadata-imds-ak-leakage-istio-route-localnet]] — Veja também: CDK: Auditoria de **Cloud Metadata API (IMDS)**, Varredura de Chaves (**`ak-leakage`**), Sidecar **Istio (`istio-check`)** e `route_localnet` (`CVE-2020-8558`).
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
