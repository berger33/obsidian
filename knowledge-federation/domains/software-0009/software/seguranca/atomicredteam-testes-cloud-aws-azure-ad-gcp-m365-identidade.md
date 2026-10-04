---
id: software.seguranca.tranche12.001115
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

# Testes Atômicos de **Nuvem e Identidade** (`iaas:aws`, `iaas:azure`, `iaas:gcp`, `azure-ad`, `office-365`, `google-workspace`)

## Em uma frase
Como validar se os seus alertas de **CloudTrail**, **Microsoft Entra ID (Azure AD) Audit/Sign-in Logs**, **Google Workspace Audit Logs** e **GCP Cloud Audit Logs** realmente disparam quando um atacante cria uma chave de acesso em outro usuário IAM, adiciona uma credencial de aplicativo OAuth no Entra ID ou cria uma regra de redirecionamento de e-mail oculta no Exchange Online?

## Por que importa
O Atomic Red Team inclui plataformas dedicadas de nuvem e SaaS (**`iaas:aws`**, **`iaas:azure`**, **`iaas:gcp`**, **`azure-ad`**, **`office-365`** e **`google-workspace`**), cujos testes utilizam o AWS CLI, Azure CLI / PowerShell (`Az`, `Microsoft.Graph`), `gcloud` ou Terraform (como o projeto complementar **Stratus Red Team**) para reproduzir técnicas reais de ataque em contas de laboratório!

## Como funciona
Exemplos clássicos incluem **`T1098.001`** (*Additional Cloud Credentials* — adicionar `AccessKey` na AWS ou *Service Principal Secret* no Entra ID), **`T1098.003`** (*Additional Cloud Roles*), **`T1562.008`** (*Disable or Modify Cloud Logs* — parar CloudTrail ou excluir Diagnostic Settings no Azure) e **`T1114.003`** (*Email Forwarding Rule*)!

## Exemplo
```bash
# Listar todas as tecnicas do Atomic Red Team que possuem testes nativos para ambientes Cloud (AWS, Azure, GCP e Entra ID)
grep -rnE "iaas:(aws|azure|gcp)|azure-ad" ./atomic-red-team/atomics/T*/T*.yaml | cut -d: -f1 | sort -u
```

## Limites e trade-offs
Atenção ao tempo de propagação de logs em nuvem (*ingestion lag*) durante exercícios de Purple Team: enquanto um EDR de endpoint alerta em 2 a 10 segundos, eventos do **AWS CloudTrail** ou **Microsoft 365 Unified Audit Log** podem levar de **2 a 15 minutos** para chegar ao SIEM e disparar a regra Sigma correspondente!

## Como verificar
Sempre execute os `cleanup_command` de testes de nuvem para destruir imediatamente usuários IAM, grupos de segurança ou instâncias criadas no tenant de homologação.

## Conexões
- [[atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr]] — Veja também: Emulação de Adversários em **Linux, macOS e Containers** com Atomic Red Team: Persistência (`systemd`/`cron`), Credenciais e Escape de Container.
- [[atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr]] — Veja também: Logging Estruturado de Execuções (`-ExecutionLogPath`), Módulos de Log Customizados (**Syslog, JSON, CSV, Attire**) e Correlação com o SIEM.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[pacu-automacao-purple-team-aws-cloudtrail-sigma-guardduty-validacao]] — Referência cruzada direta com pacu-automacao-purple-team-aws-cloudtrail-sigma-guardduty-validacao.
- [[sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud]] — Referência cruzada direta com sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
