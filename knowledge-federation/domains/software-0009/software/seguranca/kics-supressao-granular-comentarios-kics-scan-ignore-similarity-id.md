---
id: software.seguranca.tranche09.000804
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

# KICS: Governança de Exceções — Comentários Inline (**`# kics-scan ignore`**) e Exclusão por **`similarityID` (`-x` / `--exclude-results`)**

## Em uma frase
Em projetos reais de infraestrutura, existem recursos que precisam de exceções legítimas e documentadas (por exemplo, o bucket S3 do site estático institucional que realmente precisa ser público na CDN, ou um DaemonSet de monitoramento eBPF que precisa de `CAP_BPF` no Kubernetes).

## Por que importa
O KICS oferece dois mecanismos auditáveis de supressão sem precisar desligar a regra inteira para o resto do repositório: **(1) Comentários Inline no código** e **(2) Exclusão por `--exclude-results <similarityID>`**!

## Como funciona
Nos comentários inline, você pode usar **`# kics-scan ignore`** no topo do arquivo (para ignorar o arquivo inteiro), **`# kics-scan ignore-block`** imediatamente antes de um recurso/bloco (para ignorar apenas aquele recurso!), ou **`# kics-scan ignore-line`** exatamente acima da linha específica!

## Exemplo
```hcl
# Exemplo de supressao cirurgica por bloco (# kics-scan ignore-block) e por linha (# kics-scan ignore-line) no Terraform
# kics-scan ignore-block
resource "aws_s3_bucket" "public_marketing_assets" {
  bucket = "corp-public-marketing-assets-2026"
}

resource "aws_security_group_rule" "bastion_ssh" {
  type        = "ingress"
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  # kics-scan ignore-line
  cidr_blocks = ["203.0.113.10/32"]
}
```

## Limites e trade-offs
Já nas pipelines de CI/CD, cada achado no JSON do KICS possui um hash determinístico de 64 caracteres chamado **`similarityID`** (que permanece estável mesmo se outras linhas do arquivo forem editadas): passar **`-x <similarityID>`** (ou listá-lo no `kics.config`) suprime exclusivamente aquela instância específica!

## Como verificar
Audite periodicamente todos os `# kics-scan ignore` no repositório com `git grep "kics-scan"` durante revisões de arquitetura.

## Conexões
- [[kics-auto-remediacao-kics-remediate-correcao-automatica-iac]] — Veja também: KICS **`remediate`**: Auto-Remediação Determinística de Misconfigurations em Infraestrutura como Código (`remediation` + `remediationType`).
- [[kics-inventario-recursos-iac-bill-of-materials-bom-m]] — Veja também: KICS: Geração de **Inventário de Recursos de Nuvem Pré-Deploy (*IaC Bill of Materials — BoM*, `-m` / `--bom`)**.
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.
- [[kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd]] — Referência cruzada direta com kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
