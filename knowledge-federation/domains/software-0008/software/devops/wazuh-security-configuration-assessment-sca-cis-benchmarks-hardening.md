---
id: software.devops.tranche20.001964
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/wazuh/wazuh/master/README.md", "https://documentation.wazuh.com/current/getting-started/components/index.html", "https://github.com/wazuh/wazuh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Wazuh Security Configuration Assessment (`SCA`): auditoria contínua de hardening e CIS Benchmarks como código

## Em uma frase
O módulo **Security Configuration Assessment (`SCA`)** do Wazuh executa varreduras periódicas nos endpoints monitorados para validar se as configurações do sistema operacional e das aplicações estão em conformidade com guias de hardening e benchmarks do **CIS (*Center for Internet Security*)**, produzindo pontuação de aprovação e recomendações de remediação.

## Por que importa
Aplicar um playbook Ansible de hardening no provisionamento inicial da máquina não garante que um administrador não tenha alterado uma flag do `/etc/ssh/sshd_config` ou um parâmetro `sysctl` manualmente meses depois.

## Como funciona
As políticas SCA são escritas em arquivos YAML declarativos contendo regras que avaliam o conteúdo de arquivos (`f:`), chaves de registro (`r:`), saída de comandos (`c:`) e processos em execução (`p:`), mapeando cada controle para padrões regulatórios (**PCI-DSS**, **NIST 800-53**, **GDPR**, **HIPAA**, **CIS**).

## Exemplo
```xml
<sca>
  <enabled>yes</enabled>
  <scan_on_start>yes</scan_on_start>
  <interval>12h</interval>
  <skip_nfs>yes</skip_nfs>
</sca>
```

## Limites e trade-offs
Por segurança, a execução de comandos dentro de políticas SCA customizadas vindas do servidor central é desabilitada por padrão no agente (`sca.remote_commands=0` em `local_internal_options.conf`).

## Como verificar
Inspecione os resultados de aprovação/falha de cada check CIS do host no módulo *Configuration Assessment* do Wazuh Dashboard.

## Conexões
- [[wazuh-vulnerability-detection-syscollector-inventario-correlacao-cve]] — Veja também: Wazuh Vulnerability Detection e `syscollector`: inventário contínuo de pacotes e correlação automatizada com bancos de CVEs.
- [[wazuh-log-analysis-decoders-rules-xml-teste-wazuh-logtest]] — Veja também: Wazuh Análise de Logs: criação de `decoders` e `rules` customizados e validação interativa com `wazuh-logtest`.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://documentation.wazuh.com/current/getting-started/components/index.html) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
