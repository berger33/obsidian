---
id: software.seguranca.tranche11.001016
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
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Workflow Avançado do Scout Suite: Reavaliação Instantânea com **`--fetch-local`**, Atualização Parcial (**`--update`**) e Exportação JSON/SQLite (`--result-format`)

## Em uma frase
Imagine que você acabou de concluir uma coleta de 25 minutos em uma conta AWS com milhares de recursos EC2, S3 e IAM, e agora quer testar três *rulesets* diferentes (o `default.json`, um ruleset de PCI-DSS e um ruleset de hardening interno) ou aplicar um arquivo de exceções revisado com o cliente.

## Por que importa
Se você rodar `scout aws` normalmente de novo, ele fará todas as milhares de chamadas de API na AWS do zero! Em vez disso, passe a flag **`--fetch-local`**: o Scout Suite carrega diretamente do disco o arquivo de dados já coletado (`scoutsuite_results_*.js`), roda apenas o `ProcessingEngine` com o novo `--ruleset` ou `--exceptions` e regenera o relatório em **menos de 2 segundos e 100% offline**!

## Como funciona
E se o engenheiro do cliente corrigiu apenas uma regra de Security Group na VPC e pediu para você revalidar sem varrer o resto da conta? Use **`--services vpc --update`**: o Scout Suite carrega o relatório local existente, consulta na nuvem **apenas o serviço `vpc`** e mescla os novos dados da VPC com os demais serviços já salvos!

## Exemplo
```bash
# Reavaliar um relatorio ja coletado em disco aplicando um novo ruleset e arquivo de excecoes 100% offline (--fetch-local)
scout aws \
  --fetch-local \
  --report-dir /cases/cloud-audit/scout-aws \
  --report-name aws-prod-2026 \
  --ruleset /etc/secops/corporate-aws-ruleset.json \
  --exceptions /cases/cloud-audit/exceptions-prod.json \
  --no-browser
```

## Limites e trade-offs
Além do formato padrão `--result-format json` (que embute o payload JavaScript para o relatório HTML estático), o `ScoutSuite/__main__.py` também suporta `--result-format sqlite` (gravando em um banco SQLite local e servindo via `Server` em `--host-ip` / `--host-port`) para contas gigantescas onde o arquivo JS excederia a memória da aba do navegador!

## Como verificar
Use `--timestamp` ao rodar auditorias periódicas para que o Scout Suite anexe automaticamente a data/hora ao nome do relatório, preservando o histórico para comparação de diffs.

## Conexões
- [[scoutsuite-customizacao-rulesets-regras-json-conditions-parametrizadas]] — Veja também: Anatomia do Motor de Regras do Scout Suite (**`Ruleset` & `ProcessingEngine`**): Como Escrever **Regras e Rulesets JSON Customizados (`--ruleset`)**.
- [[scoutsuite-gestao-excecoes-exceptions-json-mapeamento-ip-ranges]] — Veja também: Redução de Falsos Positivos e Enriquecimento de Rede no Scout Suite: Arquivos de Exceção (**`--exceptions`**) e Mapeamento de CIDRs Conhecidos (**`--ip-ranges`**).
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
