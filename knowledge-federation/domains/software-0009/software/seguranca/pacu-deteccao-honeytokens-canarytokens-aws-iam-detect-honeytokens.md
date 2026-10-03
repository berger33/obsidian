---
id: software.seguranca.tranche11.001028
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

# Detecção de **Honeytokens / Canarytokens AWS** (`iam__detect_honeytokens`) e Como Projetar **Decoys de Credenciais AWS Indetectáveis** para o Blue Team

## Em uma frase
Equipes de defesa (Blue Team / Deception Engineering) frequentemente espalham **Honeytokens (Canarytokens)** — chaves de acesso `AKIA...` falsas plantadas em arquivos `.env`, repositórios Git internos ou máquinas de desenvolvedores — que disparam um alerta crítico no SOC no exato segundo em que um invasor tenta usá-las!

## Por que importa
Porém, como o módulo **`iam__detect_honeytokens`** do Pacu consegue testar se uma chave `AKIA...` é um Honeytoken (como os gerados pelo `canarytokens.org` da Thinkst) **sem acionar o alarme do Honeytoken ou identificando a infraestrutura de engodo**?

## Como funciona
Historicamente, serviços públicos de Canarytokens criavam chaves IAM dentro de um conjunto conhecido de Account IDs da AWS ou usavam padrões de nomenclatura de usuário/ARN previsíveis; quando uma chamada como `sts:GetCallerIdentity` ou uma validação de ARN revela o Account ID e o ARN associados à chave (`aws:PrincipalAccount`), o módulo verifica se a conta ou o domínio pertence a provedores públicos de honeytokens!

## Exemplo
```bash
# Verificar no Pacu se a chave configurada na sessao apresenta indicadores conhecidos de Honeytoken / Canarytoken
pacu --session pentest-aws-lab \
  --module-name iam__detect_honeytokens \
  --exec
```

## Limites e trade-offs
Lição valiosa de **Engenharia de Deception (Blue Team)** extraída do código do `iam__detect_honeytokens`: **nunca use as contas AWS compartilhadas gratuitas do `canarytokens.org` para proteger ambientes corporativos de alto valor**! Em vez disso, crie seus Honeytokens IAM **dentro das suas próprias contas AWS de produção (ou em uma conta interna da sua AWS Organizations)**, com nomes de usuários realistas (ex.: `svc-terraform-deploy-prod`) e monitore qualquer chamada feita por essa chave (inclusive `sts:GetCallerIdentity`!) via **AWS CloudTrail + EventBridge**!

## Como verificar
Um Honeytoken criado na sua própria conta AWS com EventBridge no `sts:GetCallerIdentity` é 100% indistinguível de uma credencial real antes do primeiro uso e alerta o SOC em menos de 3 segundos!

## Conexões
- [[pacu-auditoria-lambda-env-vars-codigo-backdoor-api-gateway]] — Veja também: Auditoria e Pós-Exploração de **AWS Lambda (`lambda__enum`)** no Pacu: Extração de Código-Fonte, Variáveis de Ambiente e Riscos de `UpdateFunctionCode`.
- [[pacu-persistencia-aws-backdoor-iam-roles-users-lambda-remediacao]] — Veja também: Análise de Técnicas de **Persistência em AWS IAM** Mapeadas pelo Pacu (`iam__backdoor_*`) e Playbook de **Erradicação e Resposta a Incidentes (DFIR)**.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[pacu-gestao-credenciais-set-keys-import-keys-whoami-bruteforce-permissions]] — Referência cruzada direta com pacu-gestao-credenciais-set-keys-import-keys-whoami-bruteforce-permissions.
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Referência cruzada direta com gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
