---
id: software.seguranca.tranche09.000809
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/Checkmarx/kics/master/README.md", "https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md", "https://docs.kics.io/latest/queries/all-queries/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KICS: Detecção Integrada de **Segredos e Credenciais Hardcoded** em IaC (`passwords_and_secrets`, `--secrets-regexes-path` e `--disable-secrets`)

## Em uma frase
Arquivos de Infraestrutura como Código (`terraform.tfvars`, `docker-compose.yml`, playbooks Ansible, `values.yaml` do Helm e workflows de CI/CD) são um dos locais onde desenvolvedores mais esquecem senhas de banco de dados, tokens de API e chaves privadas SSH/TLS em texto claro.

## Por que importa
Além das mais de 2.000 queries Rego de configuração, o KICS traz integrado um **Scanner de Segredos e Senhas** que combina regras de entropia e expressões regulares (`assets/queries/common/passwords_and_secrets`) para detectar chaves AWS, GCP, Azure, GitHub, Slack, Stripe, JWTs e chaves privadas PEM dentro de qualquer arquivo IaC.

## Como funciona
Você pode fornecer um arquivo customizado de regras de segredos da sua empresa com **`--secrets-regexes-path`** ou, caso seu pipeline já execute o **Gitleaks / TruffleHog** em uma etapa dedicada e você queira evitar duplicidade, desativar a varredura de segredos do KICS com **`--disable-secrets`**.

## Exemplo
```bash
# Executar o KICS focando em segredos e credenciais hardcoded ou desativando segredos quando ja coberto pelo Gitleaks
kics scan -p /cases/iac/ansible-playbooks \
  -t Ansible \
  -o /cases/iac/out
```

## Limites e trade-offs
Mesmo que você utilize o KICS no CI/CD sobre a árvore de arquivos atual (`HEAD`), lembre-se de que o KICS inspeciona o snapshot atual dos arquivos, e **não** o histórico de commits antigos do Git (`git log`); por isso, mantenha sempre o **Gitleaks** ou **TruffleHog** para varrer o histórico completo de commits.

## Como verificar
Se um segredo de teste legítimo (ex.: chave dummy em arquivo de fixture) for reportado, suprima a linha com `# kics-scan ignore-line` ou mova para uma variável de ambiente.

## Conexões
- [[kics-auditoria-especificacoes-openapi-swagger-grpc-protobuf-apis]] — Veja também: KICS para **OpenAPI (v2/v3) e gRPC (`.proto`)**: *Shift-Left API Security* desde o Contrato da API (`--enable-openapi-refs`).
- [[kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd]] — Veja também: KICS em Pipelines CI/CD: Configuração Declarativa (`kics.config`), Códigos de Saída (**`--fail-on`**, **`--ignore-on-exit`**) e Relatórios **SARIF / SonarQube / GitLab**.
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
