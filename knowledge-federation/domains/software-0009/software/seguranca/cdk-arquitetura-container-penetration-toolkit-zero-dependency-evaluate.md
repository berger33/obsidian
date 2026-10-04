---
id: software.seguranca.tranche10.000981
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

# **CDK (`cdk-team/CDK`)**: Arquitetura do Toolkit **Zero-Dependency** em Go para Auditoria de Segurança e Pós-Exploração em Containers Slim/Distroless

## Em uma frase
Durante um pentest autorizado ou exercício de Red Team em ambientes de containers e Kubernetes, quando você obtém execução de código (RCE) dentro de um Pod moderno construído sobre imagens **Alpine, Slim ou Distroless**, quase nunca existem ferramentas básicas do sistema operacional instaladas no container (não há `curl`, `wget`, `ip`, `ifconfig`, `ps`, `netstat`, `capsh`, `fdisk` nem Python)!

## Por que importa
**CDK (*Container Penetration Toolkit*, `cdk-team/CDK`, escrito em Go estático sem dependências externas)** foi projetado especificamente para operar dentro de containers enxutos: um único binário autocontido (disponível inclusive na versão **`thin` de ~2 MB** para ambientes serverless/efêmeros!) que reúne três módulos integrados: **`cdk evaluate`** (coleta e diagnóstico automatizado de falhas de isolamento), **`cdk run <exploit>`** (execução de PoCs de escape e coleta de credenciais) e **`cdk <tool>`** (ferramentas de rede e sistema reimplementadas em Go puro)!

## Como funciona
Ao executar **`cdk evaluate`** (ou **`cdk eva --full`** para incluir varredura profunda do sistema de arquivos), o CDK inspeciona informações do SO, **Linux Capabilities habilitadas**, **Montagens (`mounts` / `docker.sock` / `hostPath`)**, **Namespaces de Rede**, variáveis de ambiente sensíveis, `route_localnet` (`CVE-2020-8558`), ServiceAccount do Kubernetes e APIs de Metadados Cloud (IMDS)!

## Exemplo
```bash
# Executar a avaliacao completa de isolamento e configuracoes inseguras dentro de um container de teste (cdk eva --full)
cdk --version
cdk eva --full
```

## Limites e trade-offs
Para equipes de **Blue Team e Engenharia de Plataforma Kubernetes**, rodar `cdk eva --full` dentro dos Pods de homologação é um excelente **Teste de Aceitação de Hardening de Containers**: ele mostra imediatamente aos engenheiros quais informações ou capacidades excessivas um invasor enxergaria caso uma aplicação web sofresse um RCE!

## Como verificar
Compare o binário completo do CDK com a build `thin` quando precisar validar detecções de EDR/eBPF (**Tracee** e **KubeArmor**) em funções FaaS.

## Conexões
- [[cdk-escapes-capabilities-cap-dac-read-search-sys-admin-sys-module-ptrace]] — Veja também: CDK & **Linux Capabilities Perigosas**: Auditoria e Exploração de **`CAP_DAC_READ_SEARCH`** (`open_by_handle_at`), **`CAP_SYS_MODULE`**, **`CAP_SYS_ADMIN`** e **`CAP_SYS_PTRACE`**.
- [[cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs]] — Referência cruzada direta com cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
