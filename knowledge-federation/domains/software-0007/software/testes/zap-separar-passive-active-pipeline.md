---
id: software.testes.tranche10.000429
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://www.zaproxy.org/docs/docker/baseline-scan/", "https://www.zaproxy.org/docs/docker/api-scan/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: separar passivo e ativo em etapas de risco distinto

## Em uma frase
Baseline passivo e varredura ativa têm efeitos e evidências diferentes e podem exigir agendas de pipeline diferentes.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Executar ataque de forma irrestrita em todo build aumenta risco e custo sem necessariamente melhorar triagem.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Rode observação passiva em fluxo frequente e reserve active scan autorizado para ambiente, alvo e janela adequados.

## Exemplo
Pull request recebe baseline; ambiente efêmero após deploy recebe API scan ativo com allowlist e relatório separado.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Separação não significa deixar findings passivos sem dono nem assumir que active scan cobre todas as categorias.

## Como verificar
Compare configuração, alvo e artifacts das duas etapas e verifique que nenhuma job usa host de produção por engano.

## Conexões
- [[zap-relatorio-artefato-e-evidencia]] — Veja também: OWASP ZAP: preservar relatório como evidência de uma execução.

## Fontes
- [OWASP ZAP — Baseline scan](https://www.zaproxy.org/docs/docker/baseline-scan/) — spider e varredura passiva sem ataques ativos; consultado em 2026-10-02.
- [OWASP ZAP — API scan](https://www.zaproxy.org/docs/docker/api-scan/) — importação de definições de API e active scanning direcionado; consultado em 2026-10-02.
