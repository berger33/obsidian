---
id: software.testes.test-data-privacy.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://csrc.nist.gov/pubs/sp/800/188/final", "https://www.nist.gov/system/files/documents/2021/05/05/NIST-Privacy-Framework-V1.0-Core-PDF.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test data management, Synthetic test data, Dados sintéticos de teste, Privacidade em dados de teste]
lote: software-testes-2000-0001
---

# Dados de teste sintéticos e proteção de privacidade

## Em uma frase
Gestão de dados de teste escolhe, minimiza, protege e elimina dados de forma compatível com o objetivo do teste, evitando exposição desnecessária de informações pessoais ou sensíveis.

## Por que importa
Copiar dados de produção para desenvolvimento ou homologação pode ampliar quem tem acesso, retenção e risco de vazamento. Dados sintéticos e técnicas de desidentificação podem reduzir exposição, mas precisam preservar propriedades relevantes para a verificação sem criar a falsa impressão de que todo dado mascarado está seguro ou representativo.

## Como funciona
NIST SP 800-188 recomenda avaliar objetivos e riscos do compartilhamento e escolher um modelo adequado, que pode incluir dados desidentificados, dados sintéticos, consultas controladas ou ambientes protegidos. O NIST Privacy Framework também recomenda inventariar dados e ações, gerir risco ao longo do ciclo de vida e manter ambientes de desenvolvimento e teste separados da produção. A escolha deve equilibrar privacidade, utilidade estatística, integridade referencial e requisitos do caso de teste.

## Exemplo
Para testar faturamento, gere contas e transações artificiais que preservem relações e distribuições necessárias ao cenário, mas não reutilizem identificadores reais. Se uma amostra desidentificada for indispensável, restrinja acesso, remova elementos não necessários, avalie risco de reidentificação e exclua cópias ao término do propósito autorizado.

## Limites e trade-offs
Remover nomes não basta: combinações de quase-identificadores podem permitir ligação com outras fontes. Dados sintéticos podem distorcer correlações e não cobrir casos raros; se forem usados como substituto de production-like data, valide utilidade para cada teste. Pseudonimização mantém possibilidade de vínculo quando existe tabela de correspondência e não equivale automaticamente a anonimização.

## Como verificar
Registre origem, classificação, finalidade, responsável, controles de acesso, retenção e método de geração ou transformação. Verifique que o conjunto não contenha segredos, identificadores ou artefatos reais fora do escopo; examine riscos de reidentificação e utilidade para os casos. Automatize limpeza e rotação dos dados de teste.

## Conexões
- [[testes-hermeticos-dependencias]] — dados isolados e declarados tornam execuções mais reproduzíveis.
- [[fixtures-pytest-ciclo-vida-escopos]] — fixtures podem criar e remover dados específicos do teste.
- [[test-oracles-resultados-esperados]] — dados sintéticos precisam de propriedades e resultados esperados coerentes.

## Fontes
- [NIST SP 800-188 — De-Identifying Government Datasets: Techniques and Governance](https://csrc.nist.gov/pubs/sp/800/188/final) — modelos de compartilhamento, dados sintéticos e limites de mascaramento; acesso em 2026-10-01.
- [NIST Privacy Framework Core v1.0](https://www.nist.gov/system/files/documents/2021/05/05/NIST-Privacy-Framework-V1.0-Core-PDF.pdf) — inventário, minimização, privacidade no ciclo de vida e separação de ambientes; acesso em 2026-10-01.
