---
id: software.seguranca.tranche11.001022
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md", "https://github.com/RhinoSecurityLabs/pacu/wiki/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Reconhecimento Furtivo de Permissões no Pacu: `set_keys`, `import_keys`, `whoami` e **`iam__bruteforce_permissions` / `iam__enum_permissions`**

## Em uma frase
No início de um exercício de Red Team ou *Assumed Breach* na AWS, o pentester frequentemente obtém uma credencial IAM (`AccessKeyId` `AKIA...` ou token temporário STS `ASIA...` extraído via SSRF/IMDS ou de um repositório Git), mas **não sabe quais permissões aquela chave possui**!

## Por que importa
Se o pentester tentar rodar `aws iam get-user` ou `aws iam list-attached-user-policies` diretamente e a chave não tiver permissão `iam:Get*`/`iam:List*`, a chamada falha com `AccessDenied` — e imediatamente dispara um alerta de reconhecimento no **Amazon GuardDuty (`Recon:IAMUser/...`)** e no SIEM!

## Como funciona
No Pacu, você importa as chaves com **`set_keys`** ou **`import_keys <perfil>`** e utiliza o módulo **`iam__enum_permissions`** (quando há acesso de leitura IAM ou para confirmar permissões e popular o objeto `whoami` no SQLite) ou **`iam__bruteforce_permissions`** (que testa chamadas de leitura de forma controlada através dos serviços selecionados para descobrir o que a chave realmente consegue acessar)!

## Exemplo
```bash
# Importar um perfil do AWS CLI para a sessao do Pacu e executar o modulo iam__enum_permissions via linha de comando
pacu --session pentest-aws-lab \
  --module-name iam__enum_permissions \
  --exec
pacu --session pentest-aws-lab --whoami
```

## Limites e trade-offs
Para **Blue Teams e Engenharia de Detecção (SOC)**: sempre que uma identidade IAM em produção gerar uma sequência rápida de eventos `AccessDenied` em múltiplos serviços distintos no CloudTrail em poucos segundos, trate isso como um indicador de alta fidelidade de enumeração automatizada de permissões (`iam__bruteforce_permissions` / `enumerate-iam`)!

## Como verificar
Use o comando `swap_keys` dentro do Pacu quando quiser alternar instantaneamente entre a chave inicial de baixo privilégio e uma nova chave obtida após escalar privilégios.

## Conexões
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Veja também: **Rhino Security Labs Pacu (`RhinoSecurityLabs/pacu`)**: Arquitetura do Framework de Pentest e Red Team para **AWS**, Sessões Isoladas e Banco **SQLite/SQLAlchemy**.
- [[pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque]] — Veja também: Escalação de Privilégio no AWS IAM com Pacu (**`iam__privesc_scan`**): Anatomia dos **21+ Vetores Clássicos de Privesc (`PassRole`, `CreatePolicyVersion`, `AttachUserPolicy`)**.
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Referência cruzada direta com gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
