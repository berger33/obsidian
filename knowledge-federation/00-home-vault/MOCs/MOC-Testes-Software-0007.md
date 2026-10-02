# MOC — Testes de Software (lote 0007)

Índice das 549 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 549 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 540 aprovadas por IA, sem converter estas últimas em aprovações humanas. Este mapa é navegação, não validação factual.

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

## Tranche 10 — frameworks, infraestrutura e ferramentas (notas 350–449)

### Selenium WebDriver: sincronização e interações no navegador
- [[selenium-explicit-wait-condicao-observavel]] — Uma espera explícita consulta uma condição definida até que ela seja verdadeira ou que o timeout configurado expire.
- [[selenium-nao-misturar-esperas-implicit-explicit]] — A espera implícita afeta buscas de elementos, enquanto a explícita aguarda uma condição específica definida pelo teste.
- [[selenium-locators-identidade-estavel]] — Locators traduzem uma propriedade observável do DOM em um alvo para interações WebDriver.
- [[selenium-findelement-find-elements-ausencia]] — findElement retorna um elemento correspondente e sinaliza ausência; findElements retorna uma lista, que pode estar vazia.
- [[selenium-stale-element-relocalizar-apos-render]] — Uma referência WebElement pode ficar obsoleta quando o nó original deixa de pertencer ao DOM ativo.
- [[selenium-frame-trocar-e-restaurar-contexto]] — O driver procura elementos no contexto de navegação atualmente selecionado; conteúdo em iframe requer troca explícita para o frame.
- [[selenium-nova-janela-diferenca-handles]] — WebDriver representa janelas e abas por handles únicos dentro da sessão e não distingue conceitualmente as duas formas.
- [[selenium-alert-wait-accept-dismiss]] — WebDriver expõe alertas, confirmações e prompts nativos por uma API específica após selecionar o alerta ativo.
- [[selenium-actions-sequencia-e-liberacao-input]] — Actions API encadeia comandos de dispositivos de entrada, como teclado, ponteiro e roda, para interações de baixo nível.
- [[selenium-elemento-interativo-validar-estado]] — Comandos de elemento incluem click, send keys, clear e ações apropriadas ao tipo do controle.

### JUnit 6.1.3: parametrização, ciclo de vida e execução
- [[junit-parametrized-test-casos-complementares]] — @ParameterizedTest executa um método repetidamente com argumentos fornecidos por uma fonte declarada.
- [[junit-methodsource-ordem-argumentos]] — MethodSource fornece os argumentos de cada invocação a partir de uma factory method compatível.
- [[junit-dynamic-test-factory-nao-e-caso]] — @TestFactory produz nós DynamicTest ou DynamicContainer em tempo de execução; a factory não é em si um caso de teste.
- [[junit-per-class-estado-compartilhado]] — O lifecycle padrão cria uma instância por método; PER_CLASS reutiliza uma instância para métodos da mesma classe.
- [[junit-parallel-opt-in-modos-e-sincronizacao]] — A execução paralela do Jupiter é opt-in; habilitar o parâmetro global não torna todos os nós concorrentes por padrão.
- [[junit-extension-parameter-resolver-explicito]] — Extensões Jupiter podem resolver parâmetros de métodos e construtores quando um ParameterResolver registrado declara suporte.
- [[junit-tempdir-escopo-e-limpeza]] — A extensão TempDir fornece diretório temporário a um campo ou parâmetro de teste.
- [[junit-tags-filtrar-testes-por-categoria]] — Tags identificam testes e podem ser usadas pelo runner para incluir ou excluir grupos durante uma execução.
- [[junit-condicional-nao-substitui-diagnostico]] — Anotações condicionais e @Disabled controlam se um teste é executado em determinado ambiente ou contexto.
- [[junit-repeated-test-invocacoes-nomeadas]] — @RepeatedTest agenda invocações repetidas de um método e pode expor o número atual e total pelo contexto de repetição.

### Mockito: isolamento de colaboradores e verificação de comportamento
- [[mockito-verificar-contrato-nao-roteiro-interno]] — verify verifica se uma interação esperada ocorreu e pode limitar a quantidade de chamadas.
- [[mockito-stubbing-nao-duplicar-verificacao]] — Stubbing define a resposta de um mock; verificar uma invocação stubada costuma ser redundante quando a saída do sistema já comprova seu uso.
- [[mockito-argumentcaptor-apos-verificacao]] — ArgumentCaptor guarda o argumento passado para uma chamada verificada para permitir assertions específicas sobre seus campos.
- [[mockito-matchers-consistencia-em-todos-argumentos]] — Quando um argumento de uma invocação usa matcher, todos os argumentos dessa mesma invocação precisam ser representados por matchers.
- [[mockito-strict-stubs-detectar-setup-morto]] — STRICT_STUBS ajuda a detectar stubs não utilizados e incompatibilidades entre argumentos configurados e invocações reais.
- [[mockito-lenient-apenas-no-stub-excepcional]] — Lenient permite que um stub escape de verificações estritas como unused stubbing ou argumento potencialmente incorreto.
- [[mockito-spy-metodo-real-e-efeitos-colaterais]] — Um spy delega chamadas não stubadas ao objeto real, diferentemente do mock que usa comportamento simulado.
- [[mockito-stubbing-consecutivo-modelar-retentativas]] — Stubbing consecutivo define respostas diferentes para chamadas subsequentes do mesmo método.
- [[mockito-nao-compartilhar-mock-mutavel-entre-testes]] — reset apaga stubbing e interações de um mock, enquanto clearInvocations limpa interações sem remover o comportamento configurado.
- [[mockito-junit-jupiter-lifecycle-explicito]] — MockitoExtension integra criação de mocks anotados e sessão Mockito ao lifecycle de testes Jupiter.

### Jest 30.5: execução assíncrona, mocks e snapshots
- [[jest-retornar-promise-para-aguardar-assercoes]] — Jest considera uma função assíncrona concluída quando sua Promise retornada resolve ou rejeita.
- [[jest-rejeicoes-async-com-rejects]] — Matchers .rejects permitem verificar o valor ou erro de uma Promise rejeitada e precisam ser retornados ou aguardados.
- [[jest-hooks-escopo-e-ordem]] — beforeAll, beforeEach, afterEach e afterAll organizam setup e cleanup no escopo em que são declarados.
- [[jest-beforeall-nao-compartilha-estado-entre-arquivos]] — beforeAll executa uma vez antes dos testes do escopo atual, não como banco de estado universal entre arquivos.
- [[jest-mock-function-calls-results-context]] — Mock functions registram chamadas, resultados, instâncias e contexto this para assertions sobre colaboração.
- [[jest-clear-reset-restore-mocks-diferencas]] — Clear apaga histórico, reset também substitui implementação configurada, e restore devolve implementação original quando a função é spy.
- [[jest-fake-timers-timers-pendentes-recursivos]] — Fake timers permitem avançar relógio JavaScript sem esperar o tempo real passar.
- [[jest-mock-modulos-esm-commonjs]] — O fluxo de mock de módulo depende do sistema de módulos e da ordem em que imports estáticos são avaliados.
- [[jest-snapshot-revisao-antes-de-atualizar]] — Snapshot armazena uma representação serializada para comparar execuções futuras e detectar mudanças de saída.
- [[jest-coverage-thresholds-nao-medir-qualidade-sozinhos]] — A configuração pode impor thresholds de cobertura globais ou para caminhos específicos e falhar quando o limite não é atingido.

### Vitest: mocks, isolamento e configuração de projetos
- [[vitest-vi-mock-hoisting-importacao]] — vi.mock é elevado pelo transformador do Vitest para executar antes dos imports estáticos do módulo de teste.
- [[vitest-domock-mock-runtime-import]] — vi.doMock registra um mock em runtime e não é içado como vi.mock.
- [[vitest-setupfiles-mocks-modulos-cache]] — Arquivos setupFiles são executados antes dos arquivos de teste e podem carregar módulos antes de um mock local.
- [[vitest-fake-timers-restaurar-relogio]] — vi.useFakeTimers substitui timers do ambiente selecionado até que o teste volte ao relógio real.
- [[vitest-setsystemtime-nao-disparar-timers]] — vi.setSystemTime altera a data percebida pelo código, mas não dispara por si só timers agendados.
- [[vitest-browser-mode-spy-namespace]] — Em Browser Mode, módulos ESM nativos têm namespace de importação que não pode ser substituído como um objeto mutável comum.
- [[vitest-projects-inheritance-opcoes-globais]] — Vitest Projects permite agrupar conjuntos de testes com opções próprias; projetos inline podem herdar configuração conforme extends.
- [[vitest-isolation-parallelism-tradeoff]] — Por padrão, o pool do Vitest isola arquivos de teste; configuração sem isolamento pode compartilhar estado de ambiente e módulos.
- [[vitest-coverage-provider-relatorio-declarado]] — Vitest suporta cobertura via provider nativo v8 ou instrumentação Istanbul, com configuração de reporters.
- [[vitest-snapshot-diff-revisao-intencional]] — Snapshots registram uma saída serializada e falham quando a nova saída difere do baseline salvo.

### Testcontainers para Java: readiness, ciclo de vida e isolamento
- [[testcontainers-startup-check-vs-readiness]] — Startup checks detectam o estado de inicialização do container; wait strategies aguardam uma condição de readiness do serviço.
- [[testcontainers-wait-endpoint-readiness-contract]] — A wait strategy pode observar condições diferentes, incluindo porta, resposta HTTP, healthcheck e logs.
- [[testcontainers-junit-static-vs-instance-containers]] — A extensão Jupiter associa containers estáticos ao ciclo de vida da classe e containers de instância ao lifecycle por teste.
- [[testcontainers-junit5-parallel-extension-limit]] — A integração JUnit Jupiter de Testcontainers documenta que execução paralela não é suportada pela extensão.
- [[testcontainers-manual-lifecycle-cleanup]] — Controle manual permite iniciar recursos fora do lifecycle automático de uma extensão e usá-los em escopo explícito.
- [[testcontainers-jdbc-url-configuracao-reprodutivel]] — O suporte JDBC permite solicitar bancos Testcontainers por URL jdbc:tc e associar o driver e módulo apropriados.
- [[testcontainers-reuse-opt-in-estado-persistente]] — Reusable Containers requer opt-in e configuração idêntica para que uma execução reutilize o recurso anterior.
- [[testcontainers-compose-espera-servico-especifico]] — A integração com Compose permite identificar serviços expostos e associar uma wait strategy ao serviço relevante.
- [[testcontainers-pinar-imagem-para-reprodutibilidade]] — Uma tag específica reduz mudanças inesperadas da imagem, enquanto um digest pode identificar exatamente o artefato resolvido.
- [[testcontainers-startup-parallel-independencia-recursos]] — Opções avançadas permitem reduzir tempo de inicialização de containers quando o setup possui serviços independentes.

### Grafana k6: modelagem de carga, métricas e thresholds
- [[k6-checks-precisam-threshold-para-falhar]] — Checks registram se uma condição observável passou, mas checks falhados não abortam nem reprovam sozinhos o teste.
- [[k6-thresholds-criterios-operacionais-pass-fail]] — Thresholds expressam condições de aprovação sobre métricas e podem afetar o resultado final de uma execução.
- [[k6-scenarios-executors-workload-nomeado]] — Scenario descreve como executar funções de teste e escolhe executor, duração, usuários ou taxa de iteração.
- [[k6-open-arrival-closed-vus]] — Executors baseados em VUs mantêm usuários virtuais que iniciam nova iteração após a anterior; arrival-rate agenda iterações por taxa.
- [[k6-dropped-iterations-capacidade-vus]] — Arrival-rate executors podem deixar de iniciar iterações quando não há VUs disponíveis ou o tempo máximo termina.
- [[k6-setup-teardown-dados-compartilhados]] — setup prepara dados antes dos cenários; seus dados JSON são copiados para cada VU e para teardown, não compartilhados como um objeto JavaScript mutável.
- [[k6-tags-segmentar-metricas-sem-alta-cardinalidade]] — Tags categorizam requests, checks, thresholds e métricas customizadas para filtragem e comparação.
- [[k6-threshold-por-tag-e-escopo-de-metrica]] — Threshold pode selecionar subconjuntos de métricas filtrando tags associadas aos samples.
- [[k6-sleep-pacing-representar-think-time]] — sleep(t) suspende o VU pelo número de segundos informado e pode representar think time quando a pausa fizer parte do workload.
- [[k6-browser-protocolo-e-experiencia-complementares]] — O módulo browser do k6 combina automação de navegador com métricas de desempenho frontend para jornadas sintéticas.

### OWASP ZAP: varredura passiva, ativa e automação segura
- [[zap-baseline-scan-passivo-sem-ataque]] — O Docker Baseline Scan realiza spidering e passive scanning, sem executar active attacks contra o alvo.
- [[zap-api-scan-definicao-e-active-scan]] — API Scan importa definições como OpenAPI, SOAP ou GraphQL e aplica varredura adaptada ao formato.
- [[zap-active-scan-autorizacao-e-ambiente]] — Active Scan envia requisições de ataque para identificar vulnerabilidades e pode alterar ou sobrecarregar o sistema alvo.
- [[zap-warnings-exitstatus-politica-ci]] — Automation Framework oferece job exitStatus para derivar o status da execução dos resultados configurados.
- [[zap-automation-framework-plano-yaml]] — Automation Framework executa jobs sequenciais a partir de um plano YAML com ambiente e configuração definidos.
- [[zap-passive-scan-wait-antes-do-relatorio]] — O job passiveScan-wait aguarda que o scanner passivo termine de processar a fila atual.
- [[zap-autenticacao-verificar-sessao-do-scan]] — ZAP suporta métodos de autenticação e verificações de sessão configurados no ambiente e no contexto.
- [[zap-alert-filter-excecao-com-justificativa]] — Alert Filters podem sobrescrever o risco de alertas de scans ativos e passivos; há regras globais e associadas a contexto.
- [[zap-relatorio-artefato-e-evidencia]] — O add-on de Report Generation produz relatórios em formatos configuráveis e tem suporte ao Automation Framework.
- [[zap-separar-passive-active-pipeline]] — Baseline passivo e varredura ativa têm efeitos e evidências diferentes e podem exigir agendas de pipeline diferentes.

### Schemathesis: geração baseada em schema e fluxos de API
- [[schemathesis-schema-inputs-e-checks]] — Schemathesis lê schema OpenAPI ou GraphQL para construir entradas e exercitar operações documentadas.
- [[schemathesis-fases-coverage-fuzzing-stateful]] — Data generation inclui estratégias e fases diferentes, como exemplos, coverage, fuzzing e execução stateful.
- [[schemathesis-valid-invalid-modes-contrato]] — Modos de geração podem focar entradas conformes ou violadoras do schema para testar aceitação e rejeição.
- [[schemathesis-shrinking-reproducao-falha]] — Shrinking busca reduzir uma entrada que reproduz uma falha para um caso menor e mais diagnóstico.
- [[schemathesis-stateful-links-sequencia-api]] — OpenAPI Links permite mapear explicitamente dados de uma resposta para parâmetros de outra operação e modelar relações stateful específicas.
- [[schemathesis-stateful-sem-link-nao-presumir]] — Schemathesis pode inferir conexões stateful por análise do schema OpenAPI, aprender relações de cabeçalhos Location no CLI e usar Links explícitos quando necessário.
- [[schemathesis-checks-server-error-schema-status]] — Checks centrais podem detectar erros do servidor, status não documentados e respostas incompatíveis com o schema.
- [[schemathesis-autenticacao-precedencia-e-sanitizacao]] — Schemathesis aceita autenticação por CLI, configuração ou mecanismo associado ao schema, com precedência definida pela ferramenta.
- [[schemathesis-pytest-parametrize-call-and-validate]] — A integração pytest parametriza testes pelas operações e oferece Case para executar e validar respostas.
- [[schemathesis-orcamento-exemplos-rate-limit]] — `generation.max-examples` limita casos da fase fuzzing por operação e sequências stateful; examples e coverage adicionam seus próprios casos.

### StrykerJS: mutation testing e interpretação de resultados
- [[stryker-dry-run-suite-original-passa]] — Stryker executa um dry run sem mutações antes de iniciar a avaliação de mutants.
- [[stryker-killed-survived-no-coverage]] — Killed indica que um teste falhou com o mutant ativo; survived e No coverage são undetected, enquanto Ignored é excluído intencionalmente da avaliação.
- [[stryker-threshold-break-falha-pipeline]] — Thresholds high e low classificam a pontuação, enquanto break pode fazer a execução terminar com erro abaixo do limite.
- [[stryker-coverage-analysis-custos-e-classificacao]] — Coverage analysis pode selecionar quais testes executar para cada mutant e distinguir categorias conforme dados do runner.
- [[stryker-incremental-resultados-cache-validade]] — Incremental mode reutiliza resultados quando arquivos mutados e testes não mudaram segundo o diff que o runner suporta.
- [[stryker-mutate-apenas-codigo-de-producao]] — A opção mutate seleciona arquivos e padrões sujeitos a alterações artificiais.
- [[stryker-ignore-mutant-justificado-e-visivel]] — Stryker permite excluir mutators, usar comentários disable ou plugins ignore para padrões específicos.
- [[stryker-static-mutants-pertest-requirement]] — StrykerJS exige coverageAnalysis perTest para ignoreStatic; mutants estáticos ignorados aparecem como Ignored e não contam no mutation score.
- [[stryker-timeout-investigar-runner-e-mutante]] — A configuração oferece limites temporais para processos de teste e execução de mutants.
- [[stryker-equivalent-mutant-score-interpretacao]] — Mutation score resume resultados de mutants no escopo selecionado, mas não classifica automaticamente equivalência semântica.

## Tranche 11 — frameworks, protocolos, carga e automação móvel (notas 450–549)

### REST Assured: contratos HTTP testáveis em Java
- [[restassured-given-when-then-fronteira]] — O padrão given/when/then organiza a especificação da requisição, a execução do HTTP e as expectativas sobre a resposta.
- [[restassured-request-specification-reuso-isolado]] — RequestSpecification agrupa dados de request que podem ser compostos e reaproveitados em várias chamadas.
- [[restassured-response-specification-contrato-comum]] — Uma response specification permite reutilizar assertions comuns para respostas de vários testes.
- [[restassured-path-query-parameters-distintos]] — Path parameters substituem segmentos nomeados do caminho; query parameters são enviados na parte de consulta da URL.
- [[restassured-object-mapping-dependencias-explícitas]] — REST Assured pode serializar objetos Java para JSON ou XML e desserializar respostas quando os mapeadores compatíveis estão disponíveis no classpath.
- [[restassured-jsonpath-extrair-depois-de-validar]] — JsonPath permite selecionar valores do corpo JSON da resposta para assertions ou etapas posteriores do teste.
- [[restassured-json-schema-validacao-opcional]] — REST Assured oferece matcher para validar um corpo JSON contra um schema, disponível pela integração de validação correspondente.
- [[restassured-filtros-logging-nao-e-wire-capture]] — Filters podem observar ou alterar request antes do envio e response antes das expectations; filtros também podem implementar logging ou autenticação.
- [[restassured-auth-por-caso-sem-credencial-em-log]] — REST Assured suporta esquemas de autenticação e configuração de credenciais por request.
- [[restassured-configuracao-global-reset-e-paralelismo]] — REST Assured expõe defaults estáticos como base URI, filtros e specifications que influenciam requests posteriores.

### WireMock: stubs HTTP, estados e diagnóstico de interações
- [[wiremock-mapping-request-response-contrato]] — Um stub WireMock associa condições de request a uma response configurada por código ou arquivo JSON.
- [[wiremock-urlpath-query-param-matching]] — WireMock permite comparar URL completa ou só o path e declarar query parameters separadamente.
- [[wiremock-json-body-matcher-estrutura]] — WireMock fornece matchers de corpo JSON que comparam conteúdo estruturado, além de comparação literal ou JSONPath.
- [[wiremock-priority-sobreposicao-stubs]] — Se múltiplos stubs combinam com uma request, a prioridade controla qual resposta é selecionada; números menores indicam prioridade maior.
- [[wiremock-scenario-maquina-de-estados]] — Um cenário WireMock representa uma máquina de estados simples; mappings podem exigir estado e mudar o estado após uma request.
- [[wiremock-verificacao-de-request-journal]] — O request journal mantém requests recebidas em memória para verificação e consulta após as chamadas do sistema sob teste.
- [[wiremock-unmatched-requests-near-miss]] — Requests sem mapping normalmente recebem 404 e podem ser consultadas como unmatched; near misses apontam mappings parecidos.
- [[wiremock-faults-para-resiliencia]] — WireMock pode simular falhas de transporte para observar como o cliente trata interrupções e respostas incompletas.
- [[wiremock-junit-extension-reset-por-teste]] — A extensão WireMock para JUnit Jupiter inicia e encerra servidor conforme lifecycle e, por padrão, reseta mappings e requests entre métodos.
- [[wiremock-response-template-dados-da-request]] — Response templating pode preencher partes da resposta com valores do contexto da request em vez de manter uma fixture fixa.

### Robot Framework 7.5: keywords, fixtures e dados de teste
- [[robot-test-case-keywords-observáveis]] — Um caso Robot Framework contém chamadas a keywords descritas nas seções de teste e executadas pelas bibliotecas importadas.
- [[robot-setup-teardown-escopo]] — Setups e teardowns podem ser definidos no nível de caso ou suite e executam keywords antes/depois da unidade configurada.
- [[robot-tags-selecao-sem-substituir-assertions]] — Tags podem classificar casos e orientar a seleção de testes durante a execução.
- [[robot-template-data-driven]] — Um test template transforma as linhas de argumentos de um caso em chamadas repetidas à keyword-template escolhida.
- [[robot-variaveis-escopo-prioridade]] — Robot Framework oferece variáveis de diferentes origens e escopos, e sua resolução depende da origem e do momento da definição.
- [[robot-resource-vs-library-import]] — Resource files compartilham user keywords e dados Robot; libraries fornecem keywords implementadas em Python ou outra integração suportada.
- [[robot-keyword-argumentos-e-conversao]] — User keywords podem receber argumentos nomeados ou posicionais e podem expor valores de retorno a outras keywords.
- [[robot-ignore-error-nao-esconder-falha]] — Run Keyword And Ignore Error captura falha de keyword e devolve status e mensagem, permitindo tratamento deliberado no fluxo.
- [[robot-wait-until-keyword-succeeds-idempotência]] — Wait Until Keyword Succeeds repete uma keyword em intervalo configurado até passar ou esgotar limite.
- [[robot-output-report-sensitive-data]] — Uma execução Robot gera output.xml e relatórios/logs configuráveis que ajudam a diagnosticar os casos executados.

### Cucumber e Gherkin: especificações executáveis sem ambiguidade
- [[cucumber-feature-scenario-executable-spec]] — Uma Feature agrupa cenários relacionados e cada Example ou Scenario descreve contexto, evento e resultado esperado em steps.
- [[cucumber-keywords-nao-fazem-parte-do-matching]] — A palavra Given, When ou Then dá semântica ao texto, mas não é usada por Cucumber para distinguir step definitions durante matching.
- [[cucumber-expressions-parametros-tipados]] — Step definitions podem usar Cucumber Expressions ou regular expressions e receber valores capturados como argumentos.
- [[cucumber-step-definitions-ambiguos-unicos]] — Cucumber precisa de uma definição única que corresponda ao texto de cada step; mais de uma correspondência impede execução inequívoca.
- [[cucumber-scenario-outline-examples-linhas]] — Scenario Outline é um template; suas steps recebem valores de placeholders e o outline executa uma vez para cada linha em Examples.
- [[cucumber-data-tables-argumento-final]] — Uma DataTable é passada como argumento multilinha final à step definition e pode ser convertida conforme sua forma e tipo.
- [[cucumber-doc-string-corpo-multilinha]] — Gherkin permite Doc Strings como argumento de step para passar texto longo, como JSON, GraphQL ou uma mensagem.
- [[cucumber-background-precondicao-compartilhada]] — Background define steps comuns executados antes dos cenários aplicáveis dentro da Feature ou Rule.
- [[cucumber-hooks-condicionais-com-tags]] — Hooks podem ser associados a expressões de tags para executar preparação ou limpeza em cenários selecionados.
- [[cucumber-tags-selecao-e-inclusao]] — Tags podem organizar features e cenários e selecionar subconjuntos de execução; expressões também podem restringir hooks.

### NUnit: parametrização, lifecycle e execução paralela
- [[nunit-test-async-await-task]] — NUnit aceita test methods async que retornam Task ou Task<T> e registra o resultado após a conclusão.
- [[nunit-testcase-cada-argumento-caso]] — TestCase fornece argumentos inline para um método parametrizado e permite que cada combinação seja descoberta como test case.
- [[nunit-testcasesource-fonte-enumeravel]] — TestCaseSource identifica campo, propriedade ou método que fornece argumentos para casos parametrizados.
- [[nunit-setup-teardown-por-caso]] — SetUp é chamado antes de cada test method e TearDown logo depois de cada test case na fixture.
- [[nunit-onetimesetup-hierarquia-fixture]] — OneTimeSetUp executa uma vez antes dos testes filhos da fixture; classes base e derivadas seguem ordem de herança documentada.
- [[nunit-setupfixture-escopo-namespace]] — SetUpFixture oferece setup e teardown únicos para fixtures pertencentes a namespace e subnamespaces na assembly.
- [[nunit-fixturelifecycle-instance-per-case]] — FixtureLifeCycle pode usar instância única por fixture ou instância nova por test case.
- [[nunit-parallelizable-nao-e-limite-de-workers]] — Parallelizable marca testes ou descendentes elegíveis para concorrência; LevelOfParallelism define o teto de workers da assembly.
- [[nunit-order-local-nao-sincroniza-conclusao]] — Order organiza quando testes ou fixtures começam dentro da suite que os contém; não ordena globalmente nem aguarda término anterior.
- [[nunit-testcontext-diagnostico-por-escopo]] — TestContext fornece dados do execution context e distingue contexto de caso em método/setup/teardown de contexto de fixture nos métodos one-time.

### xUnit.net v3: dados, fixtures e paralelismo
- [[xunit-fact-vs-theory-escopo]] — Fact representa um caso individual; Theory associa a um método conjuntos de dados que produzem invocações parametrizadas.
- [[xunit-inline-data-casos-visíveis]] — InlineData fornece argumentos constantes para Theory e cada linha representa um caso executável.
- [[xunit-memberdata-classdata-provedor-tipado]] — Theories podem obter dados de membros ou classes provedoras, separando matriz de argumentos da lógica do teste.
- [[xunit-constructor-dispose-instancia-por-teste]] — xUnit cria instância nova da classe de teste para cada test que executa; constructor e Dispose oferecem preparação e limpeza por instância.
- [[xunit-class-fixture-compartilhar-recurso]] — IClassFixture compartilha uma instância de fixture entre os testes de uma classe e a descarta depois da classe.
- [[xunit-collection-fixture-serializar-recurso]] — Collection fixtures compartilham fixture entre classes associadas à mesma collection; classes na collection deixam de executar paralelamente entre si.
- [[xunit-async-lifetime-teardown]] — xUnit oferece interfaces de lifecycle assíncrono para inicialização e limpeza; suportes de DisposeAsync diferem entre v2 e v3.
- [[xunit-paralelismo-por-collection-isolar]] — No modo collections, testes de uma collection não rodam em paralelo entre si, mas collections distintas podem concorrer.
- [[xunit-outputhelper-saida-associada]] — ITestOutputHelper fornece saída associada ao test case, enquanto Console e Trace são recursos compartilhados do processo.
- [[xunit-assert-throws-tipo-exato]] — Assert.Throws e variantes assíncronas capturam exceção da operação e permitem verificar tipo e conteúdo da falha.

### Locust: cenários de usuário e geração de carga Python
- [[locust-httpuser-nao-e-browser]] — HttpUser oferece client HTTP e mantém cookies, mas não renderiza HTML nem carrega automaticamente recursos da página como browser.
- [[locust-task-weights-probabilidade]] — Decorador @task com peso faz Locust escolher tarefas com frequência relativa entre as opções disponíveis do usuário.
- [[locust-wait-time-pos-task-nao-rps]] — wait_time é aplicado após a execução de uma tarefa; ausência de wait_time inicia a próxima task assim que a atual termina.
- [[locust-on-start-stop-lifecycle]] — on_start e on_stop são callbacks por instância de User que permitem iniciar e encerrar contexto do usuário simulado.
- [[locust-request-name-cardinalidade]] — O parâmetro name do client pode agrupar requests com paths ou query values diferentes sob um nome de estatística comum.
- [[locust-catch-response-validacao-manual]] — Cliente HTTP de Locust permite inspecionar resposta no bloco catch_response e decidir manualmente se a chamada conta como sucesso ou falha.
- [[locust-taskset-sequencia-de-tarefas]] — TaskSet organiza conjunto de tarefas e pode delegar para subtasksets; SequentialTaskSet expressa sequência declarada quando a jornada requer ordem.
- [[locust-loadtestshape-tick]] — LoadTestShape permite controlar usuários e spawn rate através de tick, que retorna a população desejada e pode terminar com None.
- [[locust-distributed-master-worker]] — Em execução distribuída, master coordena interface e spawn/stop; workers executam Users e enviam estatísticas ao master.
- [[locust-fast-httpuser-gerador-versus-alvo]] — FastHttpUser pode reduzir overhead de cliente HTTP quando Locust precisa gerar uma taxa alta de requests.

### Apache JMeter: planos de teste e carga reproduzível
- [[jmeter-threadgroup-threads-independentes]] — Cada thread de um Thread Group executa o plano de teste de forma independente e pode representar uma conexão/usuário concorrente.
- [[jmeter-timer-before-samplers-scope]] — Timer é processado antes de cada sampler dentro do escopo hierárquico, e múltiplos timers podem acumular atraso.
- [[jmeter-assertion-aplica-por-escopo]] — Assertions são executadas após samplers no escopo onde aparecem e verificam campos de request/response configurados.
- [[jmeter-csv-dataset-dados-por-thread]] — CSV Data Set Config lê registros em variáveis e normalmente fornece linhas diferentes às threads do plano.
- [[jmeter-thread-variables-properties-compartilhamento]] — Variáveis de JMeter têm escopo de thread, enquanto properties são compartilhadas entre threads do processo.
- [[jmeter-cli-para-carga-gui-para-debug]] — Manual recomenda GUI para criar/debuggar plano e CLI mode para load test com menor overhead de interface.
- [[jmeter-execution-order-processors]] — JMeter processa elementos da árvore em ordem definida, com configuration elements e preprocessors antes do sampler e postprocessors/assertions depois.
- [[jmeter-listeners-impacto-gerador]] — Listeners exibem, salvam ou processam resultados e podem consumir recursos do gerador conforme volume e formato.
- [[jmeter-transaction-controller-unidades-medicao]] — Transaction Controller agrupa samplers em transação e pode produzir sample agregado conforme modo configurado.
- [[jmeter-testplan-versioned-results]] — Plano JMX e properties determinam execução; registrar apenas arquivo de resultado não permite reproduzir configuração de carga.

### Gatling: cenários, sessão e critérios de performance
- [[gatling-scenario-exec-sequencia]] — Um ScenarioBuilder encadeia ações com exec; requests e funções executadas no cenário seguem a sequência declarada.
- [[gatling-session-estado-por-virtual-user]] — Session representa o estado de um virtual user e carrega atributos ao longo das ações do scenario.
- [[gatling-feeder-dados-variados-cache]] — Feeder fornece records aos virtual users por meio de feed e os atributos passam para Session.
- [[gatling-check-saveas-apos-sucesso]] — Checks validam request/response e podem extrair um valor para Session; saveAs só é efetivo quando check passa.
- [[gatling-assertions-criterios-de-simulacao]] — Assertions na Simulation definem critérios sobre estatísticas globais ou escopos como requests/grupos.
- [[gatling-open-closed-injection-model]] — Perfis open injetam usuários por taxa de chegada; closed model define concorrência de usuários cuja duração influencia novas iterações.
- [[gatling-groups-agregacao-por-jornada]] — Groups agrupam ações do usuário e permitem observar estatísticas relativas a uma parte nomeada do scenario.
- [[gatling-pauses-e-pacing]] — Pause modela intervalo entre ações do scenario; injection controla chegada/concorrência inicial de virtual users.
- [[gatling-protocol-config-comum]] — Protocol configuration reúne base URL, headers e opções compartilhadas que podem ser associadas a um ou mais cenários.
- [[gatling-session-debug-fora-da-carga]] — Session pode ser inspecionada durante desenvolvimento para diagnosticar feeders, expressões e check failures.

### Appium: sessões e automação móvel multiplataforma
- [[appium-driver-instalacao-modular]] — Appium separa o servidor central de drivers que implementam automação por plataforma e precisam ser instalados para criar sessões.
- [[appium-capabilities-prefix-vendor]] — Capabilities são parâmetros key-value de criação de sessão e não podem ser alteradas durante seu lifecycle; capabilities não padrão usam prefixo vendor como appium:.
- [[appium-automationname-seleciona-driver]] — appium:automationName indica qual driver deve executar comandos da sessão.
- [[appium-context-native-webview]] — Contexts representam modos de automação que o driver implementa; API permite listar, ler contexto atual e trocar para outro nome disponível.
- [[appium-session-finally-delete]] — Quickstart abre session remota e chama deleteSession ao concluir interação; lifecycle da sessão é responsabilidade do cliente de teste.
- [[appium-w3c-actions-vs-comandos-driver]] — Appium oferece comandos W3C e extensões específicas do driver; migrações podem remover endpoints touch legados e apontar alternativas.
- [[appium-parallel-device-identidade-ports]] — Capabilities como udid identificam dispositivo alvo; drivers também podem requerer portas e recursos distintos para sessões simultâneas.
- [[appium-uiautomator2-android-boundary]] — UiAutomator2 é driver oficial para Android e documenta capabilities, comandos e requisitos que não são universais a todo Appium.
- [[appium-xcuitest-ios-boundary]] — XCUITest é driver oficial para apps iOS e seus requisitos dependem do host, toolchain Apple e configuração da sessão.
- [[appium-locators-acessibilidade-contrato]] — Drivers expõem estratégias de locator dependentes da plataforma, incluindo identificadores de acessibilidade ou recursos nativos.

## Estado editorial

O gate automatizado foi aprovado por 549/549 notas e as 549 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 540 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (549 notas substantivas; 1.451 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-testes-2000-0001.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-testes-2000-0001.md) e a [reconciliação do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-11.md). Os relatórios factuais por IA são [tranches 2–3](../../exports/reports/ai-review-software-testes-2000-0001.md), [4](../../exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](../../exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](../../exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](../../exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](../../exports/reports/ai-review-software-testes-2000-0001-tranche-08.md), [9](../../exports/reports/ai-review-software-testes-2000-0001-tranche-09.md) e [10](../../exports/reports/ai-review-software-testes-2000-0001-tranche-10.md), [11](../../exports/reports/ai-review-software-testes-2000-0001-tranche-11.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).
