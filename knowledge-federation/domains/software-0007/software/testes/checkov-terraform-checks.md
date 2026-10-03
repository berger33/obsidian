---
id: software.testes.tranche19.001315
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/bridgecrewio/checkov/tree/master/checkov/terraform", "https://github.com/bridgecrewio/checkov"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: análise de configuração declarada

## Em uma frase
As verificações de configuração declarada avaliam atributos de recursos, como exposição pública, criptografia, registros e políticas de acesso.

## Por que importa
Essas verificações encontram exposição indevida antes de a infraestrutura existir, quando a correção custa apenas uma alteração de arquivo.

## Como funciona
Rode a análise no diretório da configuração, trate primeiro exposição pública e ausência de criptografia e corrija na origem do módulo.

## Exemplo
Um módulo compartilhado com política permissiva pode ser corrigido uma vez, eliminando o achado em todos os usos.

## Limites e trade-offs
Corrigir caso a caso sem tocar o módulo duplica exceções, e variáveis com valor padrão inseguro propagam o risco para todos os usos.

## Como verificar
Corrija um módulo e confirme que os achados correspondentes desaparecem de todos os diretórios que o utilizam.

## Conexões
- [[checkov-output-and-ci]] — Veja também: Checkov: publicar o resultado na esteira.
- [[checkov-kubernetes-checks]] — Veja também: Checkov: análise de manifestos de orquestração.

## Fontes
- [Checkov — Verificações Terraform](https://github.com/bridgecrewio/checkov/tree/master/checkov/terraform) — implementação das verificações de configuração declarada; consultado em 2026-10-03.
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
