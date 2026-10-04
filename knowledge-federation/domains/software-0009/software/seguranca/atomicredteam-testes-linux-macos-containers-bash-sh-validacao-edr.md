---
id: software.seguranca.tranche12.001114
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md", "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Emulação de Adversários em **Linux, macOS e Containers** com Atomic Red Team: Persistência (`systemd`/`cron`), Credenciais e Escape de Container

## Em uma frase
Muitas organizações concentram 90% dos seus testes de detecção em endpoints Windows, deixando servidores **Linux de produção, nós Kubernetes e estações macOS de desenvolvedores** com cobertura de telemetria (eBPF, Auditd, Falco, Tetragon, Wazuh) nunca testada na prática!

## Por que importa
O Atomic Red Team possui centenas de testes nativos para **`supported_platforms: [linux, macos, containers]`** usando executores `sh` e `bash`, cobrindo técnicas críticas como: **Persistência via `cron` (`T1053.003`), timers/serviços `systemd` (`T1543.002`) e `.bashrc`/`.profile` (`T1546.004`)**, **Extração de `/etc/shadow` e chaves SSH (`T1003.008`, `T1552.004`)**, **Descoberta de SUID/SGID (`T1548.001`)**, **Limpeza de `bash_history` (`T1070.003`)** e **Escape de Container (`T1611`)**!

## Como funciona
Em servidores Linux onde você não deseja instalar o PowerShell Core (`pwsh`), você pode executar esses testes diretamente com utilitários leves em Python (como o **`atomic-operator`**) ou extrair e rodar os comandos `sh`/`bash` diretamente dos YAMLs com `yq`!

## Exemplo
```bash
# Inspecionar e listar com yq todos os testes atomicos da tecnica T1053.003 (Cron) compativeis com Linux
yq '.atomic_tests[] | select(.supported_platforms[] == "linux") | {name: .name, guid: .auto_generated_guid, cmd: .executor.command}' \
  ./atomic-red-team/atomics/T1053.003/T1053.003.yaml
```

## Limites e trade-offs
Ao rodar testes atômicos de Linux em um nó de homologação Kubernetes monitorado por **Falco** ou **Tetragon**, valide se os eventos gerados incluem o contexto completo do container (`container.id`, `k8s.ns.name`, `k8s.pod.name`) e a árvore de processos pai (`parent_process`).

## Como verificar
Sempre execute o `cleanup_command` imediatamente após os testes de persistência em Linux (`crontab`, `/etc/systemd/system/`, `/etc/ld.so.preload`) para não deixar serviços órfãos rodando no servidor de laboratório.

## Conexões
- [[atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs]] — Veja também: Motor de Execução **`Invoke-AtomicRedTeam`** (PowerShell Core Multiplataforma): `-ShowDetails`, `-CheckPrereqs`, `-GetPrereqs` e `-Cleanup`.
- [[atomicredteam-testes-cloud-aws-azure-ad-gcp-m365-identidade]] — Veja também: Testes Atômicos de **Nuvem e Identidade** (`iaas:aws`, `iaas:azure`, `iaas:gcp`, `azure-ad`, `office-365`, `google-workspace`).
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
