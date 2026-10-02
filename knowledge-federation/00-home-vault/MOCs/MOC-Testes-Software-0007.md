# MOC — Testes de Software (lote 0007)

Índice das 349 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 349 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 340 aprovadas por IA, sem converter estas últimas em aprovações humanas. Este mapa é navegação, não validação factual.

## Fundamentos, processo e testware
- [[test-objectives-context]] — selecionar objetivos conforme work product, riscos e contexto.
- [[testing-principles-contextual]] — usar os sete princípios como orientação contextual.
- [[error-defect-failure-root-cause]] — distinguir erro, defeito, falha e causa raiz.
- [[testing-vs-debugging]] — separar evidência de teste da investigação/correção.
- [[fundamental-test-activities]] — planejar, analisar, desenhar, implementar, executar e concluir.
- [[test-process-context-tailoring]] — adaptar atividades à situação, sem adotar receita única.
- [[testing-roles-management-and-testing]] — distinguir responsabilidades de gestão e função técnica.
- [[testware-artifacts]] — organizar os produtos de trabalho gerados pelas atividades.

## Teste estático, feedback e revisões
- [[static-testing-work-products]] — revisar work products e aplicar análise estática sem execução.
- [[static-vs-dynamic-testing]] — combinar evidências de abordagens complementares.
- [[early-frequent-stakeholder-feedback]] — obter feedback de stakeholders ao longo do SDLC.
- [[review-process-activities]] — estruturar planejamento, leitura, comunicação e tratamento de findings.
- [[review-types-formality-purpose]] — selecionar tipo de revisão conforme objetivo e risco.
- [[review-success-factors]] — preparar participantes e medir sucesso sem avaliar indivíduos.

## Níveis de teste
- [[test-levels-overview]] — comparar os cinco níveis do CTFL e seus objetivos.
- [[component-testing-isolation]] — avaliar componentes isolados.
- [[component-integration-testing-interfaces]] — examinar interações entre componentes.
- [[system-testing-requirements]] — verificar comportamento do sistema integrado.
- [[system-integration-testing-external-systems]] — testar interfaces com sistemas/serviços externos.
- [[acceptance-testing-validation]] — validar necessidades e readiness para uso/implantação.

## SDLC, manutenção e tipos de teste
- [[sdlc-impact-on-testing]] — relaciona o ciclo de vida ao escopo, timing e abordagem.
- [[testing-sequential-and-iterative-sdlc]] — compara cadência e sobreposição das atividades.
- [[good-testing-practices-across-sdlc]] — práticas de teste úteis em vários modelos.
- [[test-first-approaches-tdd-atdd-bdd]] — situa TDD, ATDD e BDD.
- [[test-driven-development]] — orienta código por testes escritos antes.
- [[acceptance-test-driven-development]] — deriva casos de critérios de aceitação.
- [[behavior-driven-development]] — comunica comportamento com exemplos.
- [[devops-testing-continuous-feedback]] — aproxima desenvolvimento, teste e operação.
- [[shift-left-testing]] — antecipa verificação sem retirar testes posteriores.
- [[testing-retrospectives-process-improvement]] — transforma experiência em melhorias acompanhadas.
- [[maintenance-testing-change-scope]] — considera risco e tamanho da mudança.
- [[maintenance-testing-triggers]] — cobre modificações, migrações e aposentadoria.
- [[testing-migrations-and-platform-upgrades]] — verifica ambiente e conversão de dados.
- [[retirement-testing-data-archival]] — valida arquivamento e recuperação.
- [[independence-of-testing-levels]] — compara níveis de independência.
- [[whole-team-approach-quality]] — compartilha responsabilidade quando apropriado.
- [[essential-skills-for-testers]] — mapeia competências para o trabalho de teste.
- [[functional-testing-quality-characteristics]] — verifica o que o sistema faz.
- [[nonfunctional-testing-quality-attributes]] — avalia como o sistema se comporta.
- [[confirmation-testing-after-fix]] — confirma correções.
- [[regression-testing-change-effects]] — identifica efeitos colaterais de mudanças.
- [[black-box-testing-specification-based]] — deriva testes da especificação.
- [[white-box-testing-structure-and-limits]] — usa a estrutura interna como base.
- [[experience-based-testing-techniques]] — organiza técnicas baseadas em experiência.
- [[error-guessing-experience]] — formula hipóteses a partir do histórico.
- [[checklist-based-testing]] — mantém condições focadas em uma lista.
- [[collaboration-based-test-approach]] — usa conversa para evitar defeitos.
- [[user-story-three-cs]] — organiza Card, Conversation e Confirmation.
- [[acceptance-criteria-as-test-conditions]] — trata critérios como condições testáveis.

## Papéis de revisão e suporte de ferramentas
- [[review-roles-responsibilities]] — distribui tarefas entre papéis da revisão.
- [[review-moderator-facilitator]] — facilita reuniões construtivas.
- [[review-scribe-recorder]] — registra findings e decisões.
- [[review-reviewer-role]] — examina work products e descreve anomalias.
- [[review-author-feedback-correction]] — cria e corrige o material revisado.
- [[review-leader-responsibility]] — responde pela organização geral.
- [[review-manager-resources]] — define prioridade e disponibiliza recursos.
- [[review-role-allocation-context]] — adapta a alocação ao risco e à formalidade.
- [[test-tool-categories]] — organiza categorias por atividade apoiada.
- [[test-tools-beyond-automation]] — inclui gestão, revisão e colaboração.
- [[test-tool-introduction-and-risk]] — planeja adoção, treinamento e mitigação.

## Isolamento, confiabilidade e regressão
- [[test-doubles-fakes-stubs-spies-mocks]] — escolher doubles conforme o papel e a forma de verificação.
- [[testes-hermeticos-dependencias]] — controlar e declarar dependências do ambiente.
- [[testes-flaky-determinismo]] — diagnosticar resultados inconsistentes.
- [[fixtures-pytest-ciclo-vida-escopos]] — controlar preparação, escopo e limpeza no pytest.
- [[snapshot-testing-jest-revisao]] — detectar mudanças de saída com snapshots revisados.
- [[regression-test-prioritization-risco-impacto]] — ordenar testes de regressão considerando impacto e risco.

## Seleção de dados e combinações
- [[particionamento-equivalencia-valores-fronteira]] — selecionar representantes de classes e exercitar limites.
- [[decision-table-testing-regras-condicionais]] — cobrir regras definidas por combinações de condições.
- [[combinatorial-testing-pairwise-t-way]] — cobrir interações t-way de parâmetros.

## Geração de casos, propriedades e sequências
- [[property-based-testing-hypothesis]] — expressar propriedades sobre entradas geradas.
- [[shrinking-contraexemplos-hypothesis]] — simplificar entradas que reproduzem uma falha.
- [[testes-stateful-model-based-hypothesis]] — gerar sequências de operações sobre sistemas com estado.
- [[state-transition-testing-coverage]] — derivar sequências e critérios de cobertura de modelos de estado.
- [[fuzzing-coverage-guided-libfuzzer]] — explorar caminhos com fuzzing guiado por cobertura.
- [[metamorphic-testing-oracle-relations]] — verificar relações entre execuções sem exigir oracle completo.
- [[differential-testing-comparacao-implementacoes]] — investigar divergências entre implementações equivalentes.
- [[test-oracles-resultados-esperados]] — escolher critérios para avaliar resultados de teste.

## Exploração e gestão de risco
- [[risk-based-testing-priorizacao-risco]] — concentrar esforço nos riscos de maior probabilidade e impacto.
- [[exploratory-testing-aprendizado-design-execucao]] — aprender, projetar e executar testes de forma integrada.
- [[session-based-testing-charters-debriefs]] — estruturar a exploração com missão, relato e debrief.

## Cobertura e eficácia das verificações
- [[cobertura-branches-statement-interpretacao]] — distinguir cobertura de statements e branches.
- [[mcdc-coverage-condicoes-independentes]] — verificar o efeito independente de condições lógicas.
- [[mutation-testing-eficacia-testes]] — verificar se a suíte detecta alterações de comportamento.
- [[piramide-testes-estrategia-contexto]] — distribuir testes conforme risco, custo e arquitetura.

## Acessibilidade, desempenho e resiliência
- [[teste-acessibilidade-automatizada-revisao-humana]] — combinar scanner com avaliação manual de tarefas acessíveis.
- [[performance-testing-modelagem-carga]] — modelar carga e critérios de desempenho.
- [[chaos-experiments-steady-state-blast-radius]] — testar resiliência com hipóteses e impacto controlado.

## Contratos de API e dados
- [[schema-based-api-testing-schemathesis-openapi]] — gerar casos de API a partir de um schema.
- [[test-data-privacidade-sinteticos]] — reduzir exposição e avaliar utilidade de dados de teste.

## Planejamento, controle e governança do teste
- [[test-planning-objetivos-escopo-comunicacao]] — alinhar objetivos, recursos, cronograma e comunicação.
- [[test-entry-exit-criteria]] — definir condições para iniciar e concluir atividades.
- [[test-effort-estimation-techniques]] — estimar esforço com métodos baseados em dados ou especialistas.
- [[test-case-prioritization-dependencies]] — ordenar casos considerando risco, cobertura e dependências.
- [[test-progress-metrics-relatorios-conclusao]] — monitorar resultados e comunicar progresso/encerramento.
- [[test-environment-configuration-management]] — manter versões e contexto reproduzíveis para testware.
- [[requirements-test-traceability]] — ligar base de teste, casos, resultados e defeitos.
- [[defect-report-reproducibility-severity-priority]] — registrar anomalias que possam ser reproduzidas e triadas.
- [[test-automation-investment-maintenance-risks]] — avaliar investimento, ROI e manutenção de automação.
- [[ci-feedback-testes-regressao]] — usar CI para fornecer feedback frequente e controlado.

## Desempenho: perfis de carga, percentis e testes de capacidade
- [[testes-latencia-percentis-thresholds]] — Defina limites de desempenho sobre percentis de latência, taxa de erros e objetivos de serviço, em vez de depender apenas da média.
- [[testes-correcao-funcional-sob-carga]] — Verifique respostas e invariantes funcionais enquanto o sistema atende carga, sem confundir sucesso HTTP isolado com correção do fluxo.
- [[testes-modelagem-carga-vus-taxa-chegada]] — Selecione um modelo aberto ou fechado de geração de carga de acordo com a pergunta que o teste pretende responder.
- [[testes-smoke-carga-minima-api]] — Use uma execução curta e de baixa carga para confirmar que o script, os endpoints principais e o ambiente respondem antes de testes maiores.
- [[testes-carga-media-perfil-trafego]] — Avalie o serviço com um perfil que represente tráfego típico, mix de operações e duração operacional relevante para a decisão.
- [[testes-stress-limite-capacidade]] — Aumente a carga de forma controlada acima do padrão esperado para observar degradação, ponto de saturação e recuperação.
- [[testes-spike-picos-abruptos]] — Simule uma subida rápida de carga para examinar se filas, autoscaling e dependências suportam mudanças abruptas e como o serviço se recupera.
- [[testes-soak-degradacao-temporal]] — Mantenha uma carga representativa por período prolongado para procurar degradação lenta que testes curtos não revelam.
- [[testes-breakpoint-rampa-carga]] — Aumente gradualmente a taxa ou concorrência para localizar a faixa em que o sistema deixa de cumprir critérios operacionais.
- [[testes-canary-validacao-telemetria]] — Use uma parcela controlada de tráfego real para observar se uma versão nova preserva sinais de saúde antes de ampliar o rollout.

## Acessibilidade: critérios WCAG e regressão multimodal
- [[teste-acessibilidade-navegacao-teclado]] — Verifique se ações e conteúdo operáveis podem ser alcançados e acionados sem mouse, respeitando o comportamento esperado de cada controle.
- [[teste-acessibilidade-foco-visivel-ordem]] — Examine se o foco de teclado permanece visível e percorre uma sequência que preserva significado e operabilidade.
- [[teste-acessibilidade-rotulos-erros-formulario]] — Confirme que controles têm rótulos e instruções associados e que erros identificam o campo, o problema e a forma de correção.
- [[teste-acessibilidade-nome-papel-valor]] — Valide se controles nativos e customizados expõem nome acessível, papel e estado coerentes com a função e com a interação atual.
- [[teste-acessibilidade-contraste]] — Meça contraste nas cores efetivamente renderizadas em cada estado relevante e confronte os resultados com o critério WCAG aplicável.
- [[teste-acessibilidade-reflow-zoom]] — Avalie se conteúdo e funcionalidade permanecem disponíveis quando o viewport é estreito ou o usuário amplia o conteúdo, sem exigir rolagem bidimensional indevida.
- [[teste-acessibilidade-wcag-target-size]] — Meça os alvos de entrada por ponteiro e avalie o requisito mínimo de tamanho ou as exceções de espaçamento definidas no critério.
- [[teste-acessibilidade-autenticacao-acessivel]] — Verifique se o processo de autenticação evita exigir uma função cognitiva sem alternativa ou apoio permitido pelo critério de acessibilidade aplicável.
- [[teste-acessibilidade-status-dinamico]] — Confirme que mensagens de sucesso, erro, progresso ou resultado de ação são programaticamente determináveis sem depender de uma mudança de foco.
- [[teste-acessibilidade-regressao-multimodal]] — Combine verificações automatizadas repetíveis com percursos manuais de teclado, zoom e tecnologia assistiva para detectar regressões de acesso.

## Segurança: autorização, sessão, entrada, headers e logs
- [[testes-autorizacao-horizontal-objetos]] — Verifique se uma conta autenticada consegue ler ou alterar somente os objetos pertencentes ao seu próprio escopo.
- [[testes-autorizacao-vertical-privilegios]] — Avalie se usuários de menor privilégio são impedidos de executar funções reservadas a papéis superiores, inclusive por chamadas diretas.
- [[testes-sessao-idle-timeout-replay]] — Verifique se a sessão expira por inatividade conforme a política e se um identificador invalidado não volta a autorizar requisições.
- [[testes-session-fixation-regeneracao-id]] — Confirme que uma sessão pré-autenticação não conserva o mesmo identificador depois que a identidade ou o privilégio da conta muda.
- [[testes-csrf-origem-token-cookie]] — Examine se uma operação que altera estado rejeita solicitações cross-site não autorizadas e se proteções são avaliadas no contexto real dos cookies.
- [[testes-validacao-input-reflected-xss]] — Siga entradas controladas até o contexto de saída e verifique se texto não confiável é exibido como dado, sem execução de conteúdo ativo.
- [[testes-ssrf-destino-url-egress]] — Avalie se uma funcionalidade que busca URLs limita destinos e protocolos a uma política explícita, sem alcançar recursos internos não autorizados.
- [[testes-autenticacao-rate-limit-enumeracao]] — Verifique que tentativas automatizadas são limitadas sem expor a existência de contas nem permitir que um teste cause bloqueio de usuários reais.
- [[testes-security-headers-browser]] — Inspecione cabeçalhos emitidos em respostas relevantes e valide se sua política corresponde à arquitetura e ao comportamento esperado do navegador.
- [[testes-logs-redaction-injection]] — Verifique que eventos necessários são registrados, dados secretos são excluídos ou mascarados e entradas não confiáveis não forjam registros.

## Confiabilidade, recuperação e rollout
- [[testes-degradacao-graciosa-invariantes]] — Introduza indisponibilidade ou lentidão de uma dependência e verifique se o serviço preserva operações essenciais ou comunica uma falha controlada.
- [[testes-load-shedding-limites-sobrecarga]] — Examine se, sob sobrecarga, o sistema limita trabalho e rejeita solicitações de forma controlada antes de comprometer todos os recursos.
- [[testes-retry-backoff-jitter-cascata]] — Valide que novas tentativas são limitadas, espaçadas e seguras para a operação, evitando multiplicar a carga quando uma dependência falha.
- [[testes-falha-dependencia-timeout-circuit-breaker]] — Simule timeout e falha de serviço dependente para confirmar orçamento de espera, abertura do circuit breaker e recuperação controlada.
- [[testes-restore-backup-integridade]] — Restaure um backup em ambiente isolado e confirme que dados e serviço podem ser recuperados, não apenas que o arquivo existe.
- [[testes-recuperacao-rto-rpo]] — Meça em exercício controlado se a recuperação atende objetivos declarados de tempo e perda máxima de dados, incluindo dependências necessárias.
- [[testes-canary-comparacao-baseline]] — Compare a versão canário e a versão estável por métricas e resultados sob condições suficientemente semelhantes antes de promover a mudança.
- [[testes-kubernetes-rolling-update-disponibilidade]] — Exercite uma atualização progressiva e confirme estado do Deployment, prontidão dos Pods e continuidade das operações esperadas.
- [[testes-rollback-versao-estado]] — Prove que uma implantação problemática pode ser revertida e que a versão anterior opera com o estado produzido durante a atualização.
- [[testes-probes-startup-liveness-readiness]] — Teste cada probe segundo seu propósito: permitir inicialização, reiniciar processo travado ou retirar temporariamente tráfego de instância não pronta.

## HTTP, contratos e integridade de dados
- [[testes-http-content-negotiation-vary]] — Verifique se o servidor escolhe uma representação compatível com Accept e outras preferências documentadas e se caches distinguem variantes quando necessário.
- [[testes-semantica-metodos-http-idempotencia]] — Verifique que métodos aceitos produzem os efeitos definidos pelo contrato HTTP, incluindo segurança, idempotência e resposta adequada a métodos não permitidos.
- [[testes-api-problem-details-rfc9457]] — Valide que erros publicados com Problem Details respeitam mídia, semântica HTTP e estrutura prevista no contrato, sem expor detalhes internos.
- [[testes-http-conditional-requests-etag]] — Exercite validators e precondições HTTP para detectar cache condicional e conflitos de atualização sem sobrescrever silenciosamente estado concorrente.
- [[testes-pagination-cursor-invariantes]] — Verifique que a navegação por cursor mantém ordem e cobertura previstas no contrato diante de limites, filtros e alterações concorrentes controladas.
- [[testes-api-rate-limit-429-retry-after]] — Valide a resposta à quota excedida e se clientes e caches respeitam o contrato de limitação de taxa sem retentar de forma agressiva.
- [[testes-contract-testing-compatibilidade-api]] — Combine validação de schema com interações que representam necessidades reais de consumidores para detectar incompatibilidades antes do deploy.
- [[testes-consumer-idempotency-duplicates]] — Entregue a mesma mensagem mais de uma vez e confirme que consumidor produz no máximo o efeito de negócio definido para aquele identificador.
- [[testes-consistencia-eventual-convergencia]] — Verifique se leituras eventualmente consistentes convergem dentro do comportamento e prazo operacional declarados, sem exigir visibilidade imediata não prometida.
- [[testes-database-integrity-reconciliation]] — Verifique invariantes de dados tanto no limite transacional do banco quanto em reconciliações independentes entre fontes ou projeções.

## Tranche 8 — frameworks e plataformas de teste (100 notas)

### Playwright
- [[playwright-fixture-ciclo-vida-isolamento]] — Playwright: ciclo de vida de fixtures por teste.
- [[playwright-fixture-worker-escopo-paralelismo]] — Playwright: fixtures de worker e estado compartilhado.
- [[playwright-autenticacao-storage-state-expiracao]] — Playwright: reutilização segura de estado autenticado.
- [[playwright-teardown-recursos-externos]] — Playwright: teardown confiável de recursos externos.
- [[playwright-mock-api-contrato-resposta]] — Playwright: mocks de API alinhados ao contrato.
- [[playwright-har-replay-cobertura-rede]] — Playwright: replay de HAR para cenários de rede.
- [[playwright-status-http-vs-falha-transporte]] — Playwright: distinguir erro HTTP de falha de transporte.
- [[playwright-retries-flaky-diagnostico]] — Playwright: retries como sinal de flakiness, não correção.
- [[playwright-paralelismo-dados-exclusivos]] — Playwright: dados exclusivos para testes paralelos.
- [[playwright-locators-assertions-web-first]] — Playwright: locators resilientes e assertions web-first.

### React Testing Library
- [[rtl-interacao-user-event-fluxo-realista]] — Testing Library: interações realistas com user-event.
- [[rtl-consultas-prioridade-role-name]] — Testing Library: priorizar consultas por papel e nome.
- [[rtl-async-findby-waitfor-condicao]] — Testing Library: aguardar estado assíncrono pela condição.
- [[rtl-waitfor-sem-efeito-colateral]] — Testing Library: manter waitFor sem efeitos colaterais.
- [[rtl-formulario-erro-associacao-label]] — Testing Library: validar formulários pela relação label-controle.
- [[rtl-render-customizado-provedores-contexto]] — Testing Library: render customizado com provedores.
- [[rtl-testar-resultado-nao-implementacao]] — Testing Library: verificar resultado em vez de detalhe interno.
- [[rtl-consulta-singular-ambiguidade]] — Testing Library: detectar consultas ambíguas.
- [[rtl-fetch-loading-empty-error-states]] — Testing Library: cobrir loading, vazio e erro de carregamento.
- [[rtl-cleanup-isolamento-renderizacao]] — Testing Library: limpeza e isolamento entre renders.

### Android
- [[android-test-pyramid-escopo-runner]] — Android: escolher escopo e runner de teste.
- [[android-instrumented-sincronizacao-sem-sleep]] — Android: sincronizar testes instrumentados sem sleeps fixos.
- [[android-uiautomator-fronteira-sistema]] — Android: UI Automator para fronteiras de sistema.
- [[android-compose-semantics-assertions]] — Android Compose: testar semântica e ações expostas.
- [[android-compose-clock-idle-animacoes]] — Android Compose: controlar clock e animações em testes.
- [[android-multiplas-telas-configuracao]] — Android: cobrir tamanhos de tela e configuração.
- [[android-process-death-restauracao-estado]] — Android: testar restauração após recriação do processo.
- [[android-permissoes-recusa-revocacao]] — Android: testar concessão, recusa e revogação de permissões.
- [[android-separar-teste-ui-de-regra]] — Android: não concentrar regras de negócio em teste de UI.
- [[android-test-flakiness-reproducao-dispositivo]] — Android: tornar falhas instrumentadas reproduzíveis.

### Flutter
- [[flutter-estrategia-unit-widget-integration]] — Flutter: distribuir testes entre unit, widget e integração.
- [[flutter-plugin-channel-mock-fronteira]] — Flutter: mockar canais de plugin sem alegar teste nativo.
- [[flutter-integration-dispositivo-fluxo]] — Flutter: desenhar testes de integração em dispositivo.
- [[flutter-widget-lista-rolagem-scrolluntilvisible]] — Flutter: testar listas longas sem assumir posição fixa.
- [[flutter-orientacao-layout-widget-test]] — Flutter: validar orientação retrato e paisagem.
- [[flutter-pumpandsettle-animacao-indefinida]] — Flutter: evitar pumpAndSettle em animações sem fim.
- [[flutter-finders-chaves-vs-texto]] — Flutter: escolher Finder por semântica, texto ou chave.
- [[flutter-testwidgets-pump-microtasks]] — Flutter: sincronizar pump e atualizações assíncronas.
- [[flutter-widget-erro-overflow-responsivo]] — Flutter: detectar overflow e conteúdo inacessível em widget tests.
- [[flutter-mocks-plugin-versus-device-regressao]] — Flutter: separar contrato simulado de regressão em dispositivo.

### Terraform
- [[terraform-validate-vs-test-provisionamento]] — Terraform: distinguir validate de terraform test.
- [[terraform-tests-mock-provider-escopo]] — Terraform: delimitar mocks de provider.
- [[terraform-test-run-apply-cleanup]] — Terraform: isolar testes que aplicam infraestrutura.
- [[terraform-variable-validation-contract]] — Terraform: testar validação de variáveis como contrato.
- [[terraform-check-block-nao-blocking]] — Terraform: interpretar check blocks sem tratá-los como preconditions.
- [[terraform-outputs-sensitive-testes]] — Terraform: testar outputs sem expor valores sensíveis.
- [[terraform-provider-lockfile-reprodutibilidade]] — Terraform: validar reprodutibilidade de providers.
- [[terraform-data-sources-outputs-mock-real]] — Terraform: testar data sources e outputs calculados.
- [[terraform-plan-assertions-estado-esperado]] — Terraform: verificar plano contra mudança de infraestrutura esperada.
- [[terraform-sandbox-isolamento-paralelo]] — Terraform: isolar sandboxes de testes paralelos.

### Kafka
- [[kafka-producer-idempotencia-retries-acks]] — Kafka: testar produtor idempotente e confirmação.
- [[kafka-ordering-partition-retries]] — Kafka: delimitar ordenação por partição.
- [[kafka-transactional-producer-consumer-read-committed]] — Kafka: testar transações com consumidor read-committed.
- [[kafka-offset-commit-proximo-registro]] — Kafka: verificar semântica de offset committed.
- [[kafka-at-least-once-consumidor-idempotente]] — Kafka: tornar efeitos do consumidor seguros contra redelivery.
- [[kafka-rebalance-processamento-em-curso]] — Kafka: testar rebalance com processamento em andamento.
- [[kafka-retry-dlq-erro-transitorio-permanente]] — Kafka: separar erro transitório de erro permanente.
- [[kafka-producer-callback-delivery-failure]] — Kafka: observar falhas de entrega no produtor.
- [[kafka-consumer-reset-start-offset]] — Kafka: testar offset inicial e política de reset.
- [[kafka-testcontainers-contrato-broker]] — Kafka: escolher broker de teste conforme contrato.

### Machine learning
- [[ml-feature-schema-contract-validacao]] — ML: validar schema de features antes do serving.
- [[ml-training-serving-skew-transformacao]] — ML: detectar divergência entre transformação de treino e serving.
- [[ml-data-leakage-split-temporal]] — ML: testar vazamento de informação entre splits.
- [[ml-reproducibilidade-seed-ambiente-artefatos]] — ML: tornar experimentos e artefatos reproduzíveis.
- [[ml-calibracao-limiares-decisao]] — ML: testar calibração e limiares de decisão.
- [[ml-monitoring-drift-feature-label]] — ML: monitorar drift sem confundir com queda de qualidade.
- [[ml-batch-online-paridade-predicoes]] — ML: comparar predição batch e online.
- [[ml-model-serving-fallback-timeout]] — ML: testar timeout e fallback de serving.
- [[ml-numerica-tolerancia-estabilidade]] — ML: definir tolerância para comparações numéricas.
- [[ml-canary-release-rollback-metricas]] — ML: liberar modelo por canário e critério de rollback.

### GitHub Actions
- [[gha-minimum-token-permissions]] — GitHub Actions: limitar permissões do token GITHUB_TOKEN.
- [[gha-script-injection-event-context]] — GitHub Actions: evitar injeção em scripts com contexto de evento.
- [[gha-pinning-third-party-actions]] — GitHub Actions: fixar e revisar actions de terceiros.
- [[gha-secrets-pull-request-forks]] — GitHub Actions: proteger secrets em pull requests externos.
- [[gha-concurrency-cancel-deployments]] — GitHub Actions: configurar concurrency sem cancelar release válida.
- [[gha-artifact-retention-provenance]] — GitHub Actions: reter artifacts sem perder proveniência.
- [[gha-environment-protection-gates]] — GitHub Actions: verificar gates de environment antes do deploy.
- [[gha-matrix-fail-fast-coverage]] — GitHub Actions: desenhar matrix que detecta incompatibilidade.
- [[gha-job-output-untrusted-artifacts]] — GitHub Actions: não confiar em artifacts de execução não privilegiada.
- [[gha-path-filters-ci-cobertura]] — GitHub Actions: testar path filters e caminhos de validação.

### Prometheus
- [[prometheus-alert-rule-unit-test-input-series]] — Prometheus: testar alert rules com séries controladas.
- [[prometheus-alert-for-pending-firing]] — Prometheus: cobrir estados pending e firing de alertas.
- [[prometheus-alert-labels-annotations-invariantes]] — Prometheus: validar labels e annotations de alertas.
- [[prometheus-recording-rule-expression-output]] — Prometheus: testar recording rules e série resultante.
- [[prometheus-rate-counter-reset]] — Prometheus: testar rate diante de reset de counter.
- [[prometheus-vector-vazio-vs-zero]] — Prometheus: diferenciar vetor vazio de valor zero.
- [[prometheus-aggregation-labels-cardinality]] — Prometheus: testar agregação e preservação de labels.
- [[prometheus-alert-no-data-scrape-failure]] — Prometheus: separar condição saudável de ausência de telemetria.
- [[prometheus-rule-test-boundary-time-window]] — Prometheus: cobrir fronteiras de janela em testes de regras.
- [[prometheus-promtool-ci-rule-validation]] — Prometheus: executar promtool no CI para regras versionadas.

### Docker
- [[docker-build-context-dockerignore-audit]] — Docker: auditar build context e .dockerignore.
- [[docker-multistage-runtime-minimo]] — Docker: verificar fronteira entre build stage e runtime.
- [[docker-base-image-digest-atualizacao]] — Docker: controlar base image e processo de atualização.
- [[docker-build-checks-lint-dockerfile]] — Docker: executar build checks para detectar erros de Dockerfile.
- [[docker-build-secrets-nao-arg-env]] — Docker: não inserir secrets em ARG, ENV ou layers.
- [[docker-container-nonroot-permissions]] — Docker: testar execução com usuário não privilegiado.
- [[docker-runtime-healthcheck-supervision]] — Docker: validar healthcheck sem confundi-lo com readiness.
- [[docker-image-test-smoke-entrypoint]] — Docker: testar a imagem final com smoke test.
- [[docker-cache-reproducibilidade-build]] — Docker: testar cache sem depender dele para correção.
- [[docker-image-sbom-provenance-release]] — Docker: associar imagem publicada a versão e proveniência.

## Tranche 9 — frameworks, protocolos e infraestrutura de teste (100 notas)

### Cypress
- [[cypress-test-isolation-indexeddb]] — Cypress: entender o alcance do test isolation.
- [[cypress-query-retry-sem-repetir-efeitos]] — Cypress: distinguir retryability de queries e efeitos.
- [[cypress-intercept-browser-vs-cy-request]] — Cypress: cy.intercept observa tráfego do app, não cy.request.
- [[cypress-register-intercept-before-trigger]] — Cypress: registrar intercept antes da ação que dispara a rede.
- [[cypress-stub-versus-real-server-coverage]] — Cypress: equilibrar stubs de rede e fluxo com servidor real.
- [[cypress-session-cache-validacao]] — Cypress: validar uma sessão restaurada por cy.session.
- [[cypress-cross-origin-cy-origin]] — Cypress: cruzar origens com cy.origin no mesmo teste.
- [[cypress-clock-timers-date]] — Cypress: controlar relógio sem mascarar espera externa.
- [[cypress-component-testing-boundary]] — Cypress: separar component testing de cobertura end-to-end.
- [[cypress-test-retries-diagnostico]] — Cypress: interpretar test retries como sinal de flakiness.

### Pact
- [[pact-consumer-request-as-sent]] — Pact: capturar a requisição que o cliente realmente envia.
- [[pact-matchers-consumer-relevant]] — Pact: escolher matchers por relevância para o consumidor.
- [[pact-not-functional-provider-test]] — Pact: não usar contrato como teste funcional do provider.
- [[pact-provider-verify-local-instance]] — Pact: verificar contracts contra instância local do provider.
- [[pact-provider-state-setup-per-interaction]] — Pact: preparar provider states determinísticos por interação.
- [[pact-provider-state-false-positive-params]] — Pact: evitar falso positivo por parâmetro de busca ignorado.
- [[pact-stub-below-request-validation]] — Pact: manter stubs abaixo da validação do request.
- [[pact-publish-version-verification-matrix]] — Pact: publicar versões e resultados para compatibilidade.
- [[pact-can-i-deploy-environment-context]] — Pact: testar can-i-deploy contra o ambiente real de destino.
- [[pact-webhook-provider-verification-feedback]] — Pact: tratar webhook como gatilho, não resultado de verificação.

### PostgreSQL
- [[postgresql-read-committed-snapshot-por-statement]] — PostgreSQL: testar snapshots no READ COMMITTED.
- [[postgresql-serializable-retry-serialization-failure]] — PostgreSQL: repetir transação após serialization failure.
- [[postgresql-mvcc-concurrent-read-write]] — PostgreSQL: testar visibilidade MVCC entre conexões.
- [[postgresql-unique-constraint-concorrencia]] — PostgreSQL: validar unicidade sob inserções concorrentes.
- [[postgresql-row-lock-skip-locked-queue]] — PostgreSQL: testar filas com FOR UPDATE SKIP LOCKED.
- [[postgresql-deadlock-sqlstate-retry]] — PostgreSQL: reproduzir deadlock e repetir operação inteira.
- [[postgresql-explain-analyze-execucao-side-effects]] — PostgreSQL: tratar EXPLAIN ANALYZE como execução.
- [[postgresql-sequence-valores-nao-gapless]] — PostgreSQL: não testar sequences como contador sem lacunas.
- [[postgresql-timestamptz-session-timezone]] — PostgreSQL: testar timestamptz com timezone explícito.
- [[postgresql-sqlstate-assertion-errors]] — PostgreSQL: afirmar SQLSTATE em vez de texto de erro.

### GraphQL
- [[graphql-validation-before-resolvers]] — GraphQL: validar operações antes de executar resolvers.
- [[graphql-variable-omitted-null-default]] — GraphQL: distinguir variável omitida de null explícito.
- [[graphql-non-null-null-propagation]] — GraphQL: testar propagação de null em campos non-null.
- [[graphql-partial-data-errors-path]] — GraphQL: aceitar data parcial quando um resolver falha.
- [[graphql-alias-fragment-response-shape]] — GraphQL: testar aliases e fragments pela forma da resposta.
- [[graphql-pagination-cursor-invariants]] — GraphQL: validar invariantes da paginação por cursor.
- [[graphql-dataloader-request-scope]] — GraphQL: testar batching sem compartilhar cache entre usuários.
- [[graphql-authorization-resolver-context]] — GraphQL: verificar autorização no caminho de execução.
- [[graphql-cache-control-private-identities]] — GraphQL: testar cache em respostas autenticadas.
- [[graphql-schema-change-compatibility]] — GraphQL: revisar mudanças de schema com operações consumidoras.

### Apple XCTest
- [[xctest-async-await-test-method]] — XCTest: usar async/await em testes assíncronos Swift.
- [[xctest-expectation-fulfillment-count]] — XCTest: controlar fulfillment e over-fulfillment de expectations.
- [[xctest-waiter-group-timeout]] — XCTest: aguardar grupo de expectativas com resultado explícito.
- [[xctest-ui-accessibility-identifiers]] — XCTest UI tests: selecionar controles por identificadores estáveis.
- [[xctest-app-launch-arguments-environment]] — XCTest UI tests: configurar o app por launch arguments.
- [[xctest-plans-matrix-configurations]] — Xcode test plans: variar configurações de execução intencionalmente.
- [[xctest-signpost-performance-metric]] — XCTest: medir intervalo instrumentado com signpost metric.
- [[xctest-order-independent-state-reset]] — XCTest: não depender da ordem dos métodos de teste.
- [[xctest-locale-device-configuration]] — XCTest: cobrir locale e device sem depender do simulador anterior.
- [[xctest-ui-wait-for-condition-not-sleep]] — XCTest UI tests: aguardar condição da interface, não sleep.

### Kubernetes
- [[kubernetes-job-completion-backoff]] — Kubernetes Job: testar conclusão e retries do controller.
- [[kubernetes-cronjob-no-exactly-once]] — Kubernetes CronJob: testar execução idempotente, não exactly-once.
- [[kubernetes-deployment-rollout-observed-state]] — Kubernetes Deployment: aguardar rollout e validar aplicação.
- [[kubernetes-networkpolicy-plugin-enforcement-test]] — Kubernetes NetworkPolicy: testar enforcement do plugin de rede.
- [[kubernetes-rbac-auth-can-i-identity]] — Kubernetes RBAC: verificar permissão com identidade e escopo.
- [[kubernetes-pdb-voluntary-disruption-test]] — Kubernetes PDB: limitar disrupção voluntária em teste controlado.
- [[kubernetes-hpa-eventual-convergence]] — Kubernetes HPA: testar convergência eventual de réplicas.
- [[kubernetes-configmap-env-vs-volume]] — Kubernetes ConfigMap: testar atualização por env e por volume.
- [[kubernetes-namespace-cleanup-isolation]] — Kubernetes: isolar testes de cluster por namespace descartável.
- [[kubernetes-service-endpoints-readiness]] — Kubernetes Service: testar endpoints prontos sem fixar IP de Pod.

### OpenTelemetry
- [[otel-inmemory-span-exporter-assertions]] — OpenTelemetry: inspecionar spans com exporter em memória.
- [[otel-span-error-status-exception]] — OpenTelemetry: testar exceção e status de span separadamente.
- [[otel-context-propagation-async-boundary]] — OpenTelemetry: preservar contexto em fronteira assíncrona.
- [[otel-resource-scope-instrumentation-identity]] — OpenTelemetry: distinguir resource de instrumentation scope.
- [[otel-inmemory-metrics-reader-aggregation]] — OpenTelemetry: testar agregação de métricas em memória.
- [[otel-histogram-buckets-boundaries]] — OpenTelemetry: testar histograma por limites e distribuição.
- [[otel-log-trace-correlation-context]] — OpenTelemetry: verificar correlação de logs com trace ativo.
- [[otel-cardinality-views-attribute-control]] — OpenTelemetry: testar cardinalidade e views de métricas.
- [[otel-test-provider-exporter-lifecycle]] — OpenTelemetry: isolar exporter e provider entre testes.
- [[otel-semconv-versioned-attributes]] — OpenTelemetry: versionar assertions de semantic conventions.

### pytest
- [[pytest-tmp-path-per-test-files]] — pytest: usar tmp_path para arquivos isolados por teste.
- [[pytest-tmp-path-factory-session-data]] — pytest: reservar tmp_path_factory para artefato caro compartilhado.
- [[pytest-yield-fixture-teardown-order]] — pytest: ordenar teardown de fixtures dependentes.
- [[pytest-fixture-scope-isolation]] — pytest: alinhar escopo de fixture ao ciclo de vida do recurso.
- [[pytest-parametrize-ids-values-reference]] — pytest: nomear parâmetros e proteger dados mutáveis.
- [[pytest-indirect-param-fixture-setup]] — pytest: usar indirect parametrization para setup configurável.
- [[pytest-autouse-fixture-hidden-side-effects]] — pytest: limitar efeitos ocultos de fixtures autouse.
- [[pytest-unittest-fixture-injection-limit]] — pytest: entender limites de fixtures em unittest.TestCase.
- [[pytest-monkeypatch-env-teardown]] — pytest: escopar monkeypatch de ambiente e dependências.
- [[pytest-xfail-strict-expected-failure]] — pytest: ativar strict para xfail não mascarar regressão.

### GitLab CI
- [[gitlab-rules-avoid-duplicate-pipelines]] — GitLab CI: testar rules para evitar pipelines duplicados.
- [[gitlab-merge-request-rules-main-config]] — GitLab CI: garantir que configuração principal habilita MR pipeline.
- [[gitlab-child-pipeline-source-parent-pipeline]] — GitLab CI: reconhecer CI_PIPELINE_SOURCE em child pipeline.
- [[gitlab-trigger-strategy-propagate-result]] — GitLab CI: propagar resultado do downstream ao pipeline pai.
- [[gitlab-needs-artifacts-explicit-dependency]] — GitLab CI: verificar que jobs recebem artifacts necessários.
- [[gitlab-cache-not-artifact]] — GitLab CI: não usar cache como evidência de build.
- [[gitlab-resource-group-serialize-deploy]] — GitLab CI: serializar deploys com resource_group.
- [[gitlab-rules-changes-path-coverage]] — GitLab CI: testar path rules para não pular validação compartilhada.
- [[gitlab-protected-variables-untrusted-pipeline]] — GitLab CI: evitar secrets em pipeline não confiável.
- [[gitlab-parallel-matrix-coverage]] — GitLab CI: validar combinações realmente cobertas por parallel matrix.

### Spring Boot
- [[spring-webmvctest-vs-springboottest]] — Spring Boot: escolher @WebMvcTest ou @SpringBootTest.
- [[spring-mockmvc-vs-random-port]] — Spring Boot: distinguir MockMvc de servidor em porta aleatória.
- [[spring-datajpatest-database-boundary]] — Spring Boot: delimitar @DataJpaTest e o banco usado.
- [[spring-testcontext-cache-dirties-context]] — Spring TestContext: controlar estado em ApplicationContext cacheado.
- [[spring-transactional-test-real-server-threads]] — Spring Boot: não presumir rollback do cliente em RANDOM_PORT.
- [[spring-testresttemplate-status-assertions]] — Spring Boot: afirmar status com TestRestTemplate explicitamente.
- [[spring-restclient-test-slice-mockserver]] — Spring Boot: usar @RestClientTest para cliente HTTP.
- [[spring-active-profiles-test-configuration]] — Spring Boot: declarar perfil de teste sem depender do ambiente local.
- [[spring-webtestclient-mock-vs-server]] — Spring Boot: testar WebTestClient em mock e servidor.
- [[spring-graphql-test-slice-boundary]] — Spring Boot: delimitar @GraphQlTest e integração GraphQL.
## Estado editorial

O gate automatizado foi aprovado por 349/349 notas e as 349 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 340 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (349 notas substantivas; 1.651 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-testes-2000-0001.md) e a [auditoria de qualidade](../../exports/reports/note-quality-software-testes-2000-0001.md). Os relatórios factuais por IA são [tranches 2–3](../../exports/reports/ai-review-software-testes-2000-0001.md), [4](../../exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](../../exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](../../exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](../../exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](../../exports/reports/ai-review-software-testes-2000-0001-tranche-08.md) e [9](../../exports/reports/ai-review-software-testes-2000-0001-tranche-09.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).
