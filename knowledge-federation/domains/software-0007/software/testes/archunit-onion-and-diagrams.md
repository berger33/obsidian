---
id: software.testes.tranche19.001344
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
fontes: ["https://www.archunit.org/userguide/html/000_Index.html", "https://github.com/TNG/ArchUnit-Examples"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ArchUnit: verificar arquitetura em cebola e diagramas

## Em uma frase
A biblioteca oferece regra pronta para o estilo em camadas concêntricas e verificação de aderência a diagrama de componentes.

## Por que importa
Verificar a aderência a um diagrama mantém a documentação de arquitetura sincronizada com o código que existe de fato.

## Como funciona
Descreva as camadas concêntricas com seus pacotes ou mantenha o diagrama versionado e aponte a verificação para ele.

## Exemplo
Uma regra pode garantir que o domínio não seja acessado por camadas externas, conforme o desenho concêntrico adotado.

## Limites e trade-offs
Diagramas desatualizados geram falhas legítimas, e a verificação só tem valor quando o diagrama é o acordo vigente do time.

## Como verificar
Atualize o diagrama com uma dependência indevida e confirme que a verificação passa a acusá-la.

## Conexões
- [[archunit-freezing]] — Veja também: ArchUnit: congelar violações existentes.
- [[archunit-test-organization]] — Veja também: ArchUnit: organizar as verificações na suíte.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — Exemplos oficiais](https://github.com/TNG/ArchUnit-Examples) — exemplos de regras e do uso de congelamento; consultado em 2026-10-03.
