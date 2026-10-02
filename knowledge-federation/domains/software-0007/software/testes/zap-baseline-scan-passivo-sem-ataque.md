---
id: software.testes.tranche10.000420
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
fontes: ["https://www.zaproxy.org/docs/docker/baseline-scan/", "https://www.zaproxy.org/docs/desktop/addons/report-generation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OWASP ZAP: entender o limite do baseline scan

## Em uma frase
O Docker Baseline Scan realiza spidering e passive scanning, sem executar active attacks contra o alvo.

## Por que importa
Scans de segurança diferem no risco e na evidência que produzem; separar observação passiva de ataque ativo protege sistemas e melhora interpretação. Um baseline pode ser apropriado como observação inicial em CI, mas não deve ser apresentado como teste ativo de todas as vulnerabilidades.

## Como funciona
Defina alvo, autorização, autenticação, política e espera de jobs em plano reproduzível; preserve alertas e resultados para triagem. Use-o para coletar alertas passivos em alvo autorizado e interprete o resultado conforme o comportamento padrão de warnings.

## Exemplo
Um job roda baseline em staging, arquiva o relatório e agenda triagem dos alertas sem afirmar que o endpoint foi explorado.

## Limites e trade-offs
ZAP encontra sinais sujeitos a falso positivo e cobertura incompleta; scan passivo não substitui análise ativa autorizada nem revisão manual. Passividade reduz risco de impacto, mas também deixa classes de falhas que exigem ataques controlados fora dessa varredura.

## Como verificar
Confira modo de scan, alvo, saída e política de warnings no script antes de habilitar o job em pipeline.

## Conexões
- [[zap-api-scan-definicao-e-active-scan]] — Veja também: OWASP ZAP: tratar API scan como active scan.

## Fontes
- [OWASP ZAP — Baseline scan](https://www.zaproxy.org/docs/docker/baseline-scan/) — spider e varredura passiva sem ataques ativos; consultado em 2026-10-02.
- [OWASP ZAP — Report Generation](https://www.zaproxy.org/docs/desktop/addons/report-generation/) — templates em formatos variados e suporte ao Automation Framework; consultado em 2026-10-02.
