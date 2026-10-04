---
id: software.seguranca.tranche02.000117
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md", "https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/", "https://github.com/coreruleset/coreruleset"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP CRS Rule Exclusion Packages e CRS v4 Plugins: perfis oficiais de exclusão para WordPress, Nextcloud, Drupal e cPanel

## Em uma frase
O OWASP CRS fornece pacotes oficiais de exclusão de regras (*Rule Exclusion Profiles*, migrados para a arquitetura de **Plugins** no CRS v4) para aplicações web populares como **WordPress**, **Nextcloud**, **DokuWiki**, **Drupal**, **phpMyAdmin** e **XenForo**.

## Por que importa
Aplicações ricas como WordPress (no editor Gutenberg `/wp-admin` ou `wp-json`) e Nextcloud (WebDAV) enviam fragmentos HTML, XML e caminhos de arquivos complexos que acionariam dezenas de regras genéricas de XSS/SQLi/Protocolo sem um perfil pré-ajustado.

## Como funciona
Habilitando o pacote de exclusão correspondente (por exemplo `tx.crs_exclusions_wordpress=1` na regra `900130` ou instalando o plugin oficial `wordpress-rule-exclusions-plugin` na pasta `plugins/`), o CRS aplica automaticamente exceções cirúrgicas apenas para as rotas e cookies específicos daquela plataforma.

## Exemplo
```apache
# Habilitando exclusões específicas de aplicação em crs-setup.conf (ou via diretório plugins/ no CRS v4):
SecAction \
    "id:900130,\
    phase:1,\
    nolog,\
    pass,\
    t:none,\
    setvar:tx.crs_exclusions_wordpress=1"
```

## Limites e trade-offs
Ative apenas os perfis de exclusão das aplicações que realmente rodam atrás daquele virtual host WAF; nunca habilite todos os perfis simultaneamente.

## Como verificar
Verifique que a edição de um post no `/wp-admin/` ocorre sem bloqueio enquanto ataques contra `/wp-login.php` continuam bloqueados.

## Conexões
- [[owaspcrs-tratamento-falsos-positivos-ctl-ruleremovetargetbyid-before-after]] — Veja também: OWASP CRS Tuning de Falsos Positivos: `ctl:ruleRemoveTargetById` em tempo de execução (`BEFORE-CRS`) vs `SecRuleUpdateTargetById` (`AFTER-CRS`).
- [[owaspcrs-validacao-protocolo-http-911-920-metodos-content-type-charset]] — Veja também: OWASP CRS Políticas de Protocolo HTTP (`900200–900250` e `REQUEST-911`/`920`): restrição de métodos HTTP, `Content-Type` e versões TLS/HTTP.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
