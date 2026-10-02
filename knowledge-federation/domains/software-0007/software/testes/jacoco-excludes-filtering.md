---
id: software.testes.tranche15.000897
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html", "https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: excluir código gerado da medição

## Em uma frase
Exclusões podem ser configuradas por classe, pacote, anotação ou expressão, removendo do relatório código que não é alvo de teste significativo.

## Por que importa
Sem filtro, classes geradas e de configuração dominam a cobertura e distorcem limites, mas exclusão ampla demais esconde código de negócio não testado.

## Como funciona
Prefira filtros por anotação de geração ou localização claramente separada, revise cada exclusão e registre o motivo no próprio build.

## Exemplo
Excluir pacotes de clientes gerados a partir de contrato é razoável, enquanto excluir todo o pacote de serviços por conveniência remove justamente o alvo da suíte.

## Limites e trade-offs
A anotação de geração precisa aparecer na classe correta e a filtragem é aplicada de forma consistente por agente, relatório e verificação, o que exige conferir os três pontos.

## Como verificar
Remova uma exclusão, regenere o relatório e verifique qual classe entrou na conta; confirme também que a regra de verificação passou a avaliá-la.

## Conexões
- [[jacoco-merge-exec-files]] — Veja também: JaCoCo: consolidar arquivos de execução.
- [[jacoco-thresholds-policy]] — Veja também: JaCoCo: tratar cobertura como política, não como meta.

## Fontes
- [JaCoCo — jacoco:check](https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html) — regras, elementos, limites, ratios e controle de falha do build; consultado em 2026-10-02.
- [JaCoCo — jacoco:report](https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html) — formatos de relatório, fontes, agregação e configuração do goal; consultado em 2026-10-02.
