---
id: software.devops.tranche10.000960
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://www.infracost.io/docs/", "https://www.infracost.io/docs/features/cli_commands/", "https://github.com/infracost/infracost"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Infracost: consultas instantâneas sobre resultados em cache (infracost inspect) e precificação via pipe (infracost price)

## Em uma frase
O par de comandos **`infracost inspect`** e **`infracost price`** permite explorar interativamente o último scan salvo em cache (filtrando e agrupando recursos sem reprocessar o IaC) ou calcular o custo de um trecho de código IaC avulso enviado diretamente pelo `stdin`.

## Por que importa
Durante uma sessão de otimização de custos ou quando um script/agente gera um bloco `resource "aws_db_instance" "main" { ... }` em memória e quer saber quanto aquele recurso específico custaria antes mesmo de salvá-lo em um arquivo de projeto completo, usar `infracost price` via `stdin` ou consultar o cache via `infracost inspect` dá resposta imediata.

## Como funciona
Conforme descrito na seção `Analyze infrastructure` da documentação `CLI commands` (`infracost.io/docs/features/cli_commands/`): (1) após rodar `infracost scan`, todos os recursos precificados e resultados de políticas ficam cacheados localmente; invocar **`infracost inspect`** (com suas opções de filtro, agrupamento e resumo, além de `--json` ou `--llm`) lê diretamente esse cache de forma instantânea; e (2) invocar **`infracost price`** lê definições de IaC passadas pela entrada padrão (`stdin` via pipe `|`), calcula o preço daqueles recursos e imprime a estimativa imediatamente no `stdout`.

## Exemplo
```bash
# Estimar rapidamente o custo de um recurso Terraform avulso enviado via stdin com infracost price
cat << 'EOF' | infracost price
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "m6i.xlarge"
}
EOF
```

## Limites e trade-offs
Como o comando `infracost inspect` opera exclusivamente sobre os dados armazenados pelo último `infracost scan`, se você editar seus arquivos `.tf` no disco e rodar apenas `infracost inspect` sem rodar `infracost scan` novamente, o `inspect` exibirá os valores do scan anterior em cache; lembre-se de reexecutar `infracost scan` sempre que alterar os arquivos de infraestrutura.

## Como verificar
Execute o exemplo de `infracost price` acima via pipe no terminal e verifique a estimativa de custo mensal retornada para a instância `m6i.xlarge`.

## Conexões
- [[infracost-suporte-multiac-terraform-terragrunt-cloudformation-cdk]] — Veja também: Infracost: suporte multi-ferramenta de IaC (Terraform, Terragrunt, CloudFormation e AWS CDK) e multi-cloud.
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.
- [[infracost-comandos-cli-scan-inspect-price-flags-globais]] — Referência cruzada direta com infracost-comandos-cli-scan-inspect-price-flags-globais.
- [[infracost-integracao-agentes-ia-skills-claude-copilot-cursor]] — Referência cruzada direta com infracost-integracao-agentes-ia-skills-claude-copilot-cursor.

## Fontes
- [Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)](https://www.infracost.io/docs/) — Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests; consultado em 2026-10-03.
- [Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)](https://www.infracost.io/docs/features/cli_commands/) — Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency); consultado em 2026-10-03.
- [Infracost — Official GitHub Repository](https://github.com/infracost/infracost) — Repositório oficial do Infracost; consultado em 2026-10-03.
