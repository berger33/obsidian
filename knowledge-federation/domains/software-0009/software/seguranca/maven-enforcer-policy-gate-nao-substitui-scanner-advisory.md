---
id: software.seguranca.tranche17.001690
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/index.html", "https://dependency-check.github.io/DependencyCheck/dependency-check-maven/index.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Maven Enforcer e scanners de CVE: policy de build não equivale a análise de advisories

## Em uma frase
O Enforcer pode aplicar regras sobre coordenadas, versões e ambiente, mas um conjunto de regras não consulta automaticamente todas as bases de vulnerabilidades.

## Por que importa
Uma compilação verde sob convergence e versão fixa não prova ausência de CVEs ou que dependências transitivas estão atualizadas.

## Como funciona
Mantenha scanner de dependências separado, correlacione grafo e lock state e use Enforcer para requisitos que ele expressa de forma confiável.

## Exemplo
Um pipeline pode falhar por versão dinâmica no Enforcer e, em estágio próprio, publicar advisories do scanner com seus identificadores e severidades.

## Limites e trade-offs
A cobertura do scanner depende de dados, formatos e plugins adicionais; o Enforcer sozinho só aplica suas regras declaradas.

## Como verificar
Crie um teste com dependência conhecida que não viole regra de convergence e confirme que apenas o scanner de advisory a sinaliza.

## Conexões
- [[maven-enforcer-version-rule-plugin-pin-maintenance]] — Fixar a versão do Maven Enforcer Plugin e revisar mudanças de regras.

## Fontes
- [Maven Enforcer — catálogo de regras](https://maven.apache.org/enforcer/enforcer-rules/index.html) — escopo de regras de build como versions, convergence e bans; consultado em 2026-10-04.
- [OWASP Dependency-Check — Maven](https://dependency-check.github.io/DependencyCheck/dependency-check-maven/index.html) — scanner SCA que analisa dependências contra dados de vulnerabilidades; consultado em 2026-10-04.
